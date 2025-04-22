# LLM Backend Service

A FastAPI application that provides structured API endpoints for interacting with LLM models through LangChain.

## Features

- **Sentiment Analysis**: Analyzes text sentiment using the VSF-LORA model
- **Medical QA**: Answers medical multiple-choice questions using the MEDQA-LORA model
- **Instrumentation**: Prometheus metrics for monitoring
- **Tracing**: LangSmith integration for LLM observability

## Architecture

The service follows a clean, modular architecture:

- **API Layer**: FastAPI routes for each capability
- **LLM Integration**: LangChain for LLM orchestration
- **Prompting**: Structured templates for consistent model outputs
- **Output Parsing**: Custom parsers to extract relevant information

## API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /v1/sentiment`: Analyze sentiment of input text
- `POST /v1/medical-qa`: Answer medical multiple-choice questions

## Environment Variables

The service is configured using the following environment variables:

- `OPENAI_API_KEY`: API key for the LLM service
- `OPENAI_API_BASE_URL`: Base URL for the vLLM API
- `LANGSMITH_TRACING`: Enable/disable LangSmith tracing
- `LANGSMITH_API_KEY`: LangSmith API key for tracing
- `LANGSMITH_PROJECT`: LangSmith project name

## Running the Service

### Using Docker Compose

```bash
docker compose up -d
```

The API will be available at `http://localhost:8001`.

### Development Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env`

3. Run the development server:

   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8001 --reload
   ```
