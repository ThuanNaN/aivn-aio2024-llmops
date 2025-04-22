# LLM Frontend Interface

A Gradio-based web interface for interacting with fine-tuned LLM models.

## Features

- **Multiple Interfaces**: Tab-based interface for different LLM applications
- **Sentiment Analysis**: Analyze sentiment of text inputs
- **Medical QA**: Answer medical multiple-choice questions
- **Examples**: Pre-populated examples for easy testing
- **Error Handling**: Robust error handling for API failures

## Architecture

The frontend communicates with the backend API to provide:

- User-friendly interface for LLM capabilities
- Form-based input collection
- Formatted result display
- Error reporting

## Tabs

1. **Sentiment Analysis**: Analyze text sentiment as positive, negative, or neutral
2. **Medical QA**: Submit medical questions with multiple choice answers

## Environment Variables

Configure the service with:

- `OPENAI_API_BASE_URL`: URL of the OpenAPI service (vLLM)
- `BACKEND_API_URL`: URL of the backend API service
- `OPENAI_API_KEY`: API key for authorization

## Running the Service

### Using Docker Compose

```bash
docker compose up -d
```

The Gradio interface will be available at `http://localhost:7860`.

### Development Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env`

3. Run the application:

   ```bash
   python app.py
   ```

## Usage

### Sentiment Analysis

1. Navigate to the "Sentiment Analysis" tab
2. Enter text in the input field
3. Click "Analyze Sentiment"
4. View the result showing positive, negative, or neutral sentiment

### Medical QA

1. Navigate to the "Medical QA" tab
2. Enter a medical question
3. Provide four possible answer choices
4. Click "Get Answer"
5. View the selected answer
