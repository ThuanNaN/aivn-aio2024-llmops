import gradio as gr
import requests
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Configure API settings
API_BASE_URL = os.getenv("BACKEND_API_URL", None)
API_KEY = os.getenv("OPENAI_API_KEY", None)

if API_BASE_URL is None or API_KEY is None:
    raise ValueError("API_BASE_URL and API_KEY must be set in the environment variables.")

def analyze_sentiment(text):
    """
    Send a request to the sentiment analysis API and return the result.
    """
    if not text.strip():
        return "Please enter some text to analyze."
    
    url = f"{API_BASE_URL}/sentiment"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"text": text} 
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        # Check for various error conditions
        if response.status_code == 422:
            return "Backend validation error. Please check your input format."
        
        # Display raw response if not successful
        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text[:200]}"
        
        # Try to parse JSON response, with fallback for non-JSON responses
        try:
            result = response.json()
            return f"Sentiment: {result.get('content', 'Unknown')}"
        except json.JSONDecodeError:
            return f"Received non-JSON response: {response.text[:200]}"
            
    except requests.exceptions.ConnectionError:
        return "Connection error: Could not connect to the backend service. Please check if the backend is running."
    except requests.exceptions.Timeout:
        return "Request timed out. The backend service may be overloaded."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def answer_medical_question(question, choice_a, choice_b, choice_c, choice_d):
    """
    Send a request to the medical QA API and return the result.
    """
    if not question.strip():
        return "Please enter a question."
    
    url = f"{API_BASE_URL}/medical-qa"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "question": question,
        "choices": [choice_a, choice_b, choice_c, choice_d]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        # Check for various error conditions
        if response.status_code == 422:
            return "Backend validation error. Please check your input format."
        
        # Display raw response if not successful
        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text[:200]}"
        
        # Try to parse JSON response, with fallback for non-JSON responses
        try:
            result = response.json()
            return result.get("content", "No answer received")
        except json.JSONDecodeError:
            return f"Received non-JSON response: {response.text[:200]}"
            
    except requests.exceptions.ConnectionError:
        return "Connection error: Could not connect to the backend service. Please check if the backend is running."
    except requests.exceptions.Timeout:
        return "Request timed out. The backend service may be overloaded."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


# Sentiment Analysis tab
with gr.Blocks() as sentiment_tab:
    gr.Markdown("# Sentiment Analysis")
    gr.Markdown("Enter text to analyze its sentiment (positive, negative, or neutral).")
    
    with gr.Row():
        with gr.Column():
            text_input = gr.Textbox(
                label="Input Text",
                placeholder="Enter text to analyze...",
                lines=5
            )
            analyze_button = gr.Button("Analyze Sentiment")
        
        with gr.Column():
            sentiment_output = gr.Textbox(
                label="Result",
                lines=2
            )
    
    analyze_button.click(
        fn=analyze_sentiment,
        inputs=[text_input],
        outputs=[sentiment_output]
    )

    gr.Examples(
        [
            ["Thầy rất nhiệt tình và dễ thương."],
            ["Mọi thứ rất dễ hiểu."],
            ["Slide rất khó hiểu."],
            ["Thầy rất dễ thương."],
            ["Thầy rất dễ thương và nhiệt tình."],
            ["Thầy rất khó hiểu và không nhiệt tình."],
            ["Slide được cập nhật."],
        ],
        inputs=[text_input],
        outputs=[sentiment_output],
        fn=analyze_sentiment
    )

# Medical QA tab
with gr.Blocks() as medical_qa_tab:
    gr.Markdown("# Medical Question Answering")
    gr.Markdown("Enter a medical question and four possible answer choices.")
    
    question_input = gr.Textbox(
        label="Question",
        placeholder="Enter your medical question here...",
        lines=2
    )
    
    with gr.Row():
        choice_a = gr.Textbox(label="Choice A", lines=1)
        choice_b = gr.Textbox(label="Choice B", lines=1)
    
    with gr.Row():
        choice_c = gr.Textbox(label="Choice C", lines=1)
        choice_d = gr.Textbox(label="Choice D", lines=1)
    
    answer_button = gr.Button("Get Answer")
    answer_output = gr.Textbox(label="Answer", lines=2)
    
    answer_button.click(
        fn=answer_medical_question,
        inputs=[question_input, choice_a, choice_b, choice_c, choice_d],
        outputs=[answer_output]
    )
    
    gr.Examples(
        [
            ["Axonal transport is:", "Antegrade", "Retrograde", "Antegrade and retrograde", "None"],
            ["Low insulin to glucagon ratio is seen in all of these except:", "Glycogen synthesis", "Glycogen breakdown", "Gluconeogenesis", "Ketogenesis"],
        ],
        inputs=[question_input, choice_a, choice_b, choice_c, choice_d],
        outputs=[answer_output],
        fn=answer_medical_question
    )

# Create the tabbed interface
demo = gr.TabbedInterface(
    [sentiment_tab, medical_qa_tab],
    ["Sentiment Analysis", "Medical QA"]
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
