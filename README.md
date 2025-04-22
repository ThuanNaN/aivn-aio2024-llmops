# AIVN AIO 2024 LLM Ops

A comprehensive MLOps solution for deploying, serving, and monitoring fine-tuned LLMs.

## Project Overview

This project demonstrates an end-to-end LLM deployment with a focus on:

- Serving fine-tuned Llama 3.2 1B models with vLLM
- Backend API with LangChain for structured LLM interactions
- Frontend interface with Gradio
- Comprehensive monitoring with Prometheus and Grafana
- Log aggregation with Loki

## Components

- **vLLM API**: Serves the Llama 3.2 1B base model and custom LoRA adapters
- **Backend**: FastAPI service that handles prompting, model selection, and response formatting
- **Frontend**: Gradio web interface for easy interaction with the models
- **Monitoring**: Prometheus, Grafana, and Loki for observability

## Use Cases

1. **Sentiment Analysis**: Analyzes text sentiment using a fine-tuned model
2. **Medical QA**: Answers medical multiple-choice questions with domain-specific tuning

## Getting Started

1. Set up the network:

   ```bash
   docker network create aio-network
   ```

2. Start the monitoring stack:

   ```bash
   cd monitor
   docker compose up -d
   ```

3. Launch the vLLM API server:

   ```bash
   cd vllm_api
   docker compose up -d
   ```

4. Start the backend API:

   ```bash
   cd backend
   docker compose up -d
   ```

5. Launch the frontend application:

   ```bash
   cd frontend
   docker compose up -d
   ```

## Accessing Services

- **Gradio UI**: `http://localhost:7860`
- **Open WebUI**: `http://localhost:8080`
- **Grafana**: `http://localhost:3000`
- **Prometheus**: `http://localhost:9090`

## Project Structure
