from dotenv import load_dotenv
from langsmith import Client
load_dotenv()

client = Client()


# Define dataset: these are your test cases
dataset_name = "Sentiment Analysis Dataset"
dataset = client.create_dataset(dataset_name)
client.create_examples(
    dataset_id=dataset.id,
    examples=[
        {
            "inputs": {"text": "slide up đầy đủ trước mỗi buổi học ."},
            "outputs": {"sentiment": "positive"},
        },
        {
            "inputs": {"text": "lượng kiến thức quá nhiều trong một học kỳ ."},
            "outputs": {"sentiment": "negative"},
        },
        {
            "inputs": {"text": "hy vọng học kỳ sau có thể học được với cô ."},
            "outputs": {"sentiment": "positive"},
        },
        {
            "inputs": {"text": "hay , nhiệt tình , dễ hiểu ."},
            "outputs": {"sentiment": "positive"},
        },
        {
            "inputs": {"text": "phản hồi giải đáp thắc mắc cho sinh viên ."},
            "outputs": {"sentiment": "positive"},
        },
    ]
)

def correctness(inputs: dict, outputs: dict, reference_outputs: dict) -> bool:
    """Check if the model outputs are correct (i.e., match the reference outputs)."""

    for output, reference_output in zip(outputs.values(), reference_outputs.values()):
        if output != reference_output:
            return False
    return True


def concision(outputs: dict, reference_outputs: dict) -> bool:
    """Check if all model outputs are concise (i.e., exactly one word: positive, negative)."""

    allowed_responses = {"positive", "negative"}
    
    for output in outputs.values():
        output = output.strip().lower()
        if output not in allowed_responses:
            return False
    return True


def my_app(text: str) -> str:
    import requests
    url = f"http://0.0.0.0:8001/v1/sentiment"
    headers = {"Authorization": f"Bearer aio2025", "Content-Type": "application/json"}
    payload = {"text": text} 
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["content"]

def ls_target(inputs: dict) -> dict:
    return {"response": my_app(inputs["text"])}


experiment_results = client.evaluate(
    ls_target, 
    data=dataset_name, 
    evaluators=[concision, correctness],
    experiment_prefix="Llama-3.2-1B-Instruct-Sentiment",
)
