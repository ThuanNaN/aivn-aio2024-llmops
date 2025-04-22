# Serving LLMs with vLLM

This component provides high-performance inference for Llama 3.2 1B models using vLLM with LoRA adapters.

## Features

- **Base Model**: Serves Meta's Llama 3.2 1B Instruct model
- **LoRA Adapters**: Dynamically loads domain-specific fine-tuned adapters
- **OpenAI-compatible API**: Compatible with standard OpenAI client libraries
- **High Performance**: Optimized inference with continuous batching
- **Metrics**: Prometheus integration for comprehensive monitoring

## Architecture

The service uses vLLM to provide efficient inference with:

- Optimized GPU utilization
- Continuous batching for high throughput
- PagedAttention for memory efficiency
- Dynamic LoRA adapter switching

## LoRA Adapters

The service loads the following adapters at startup:

1. **MedQA Adapter**: Fine-tuned for medical multiple-choice questions
2. **VSF Adapter**: Fine-tuned for Vietnamese sentiment analysis

## Environment Variables

Configure the service with:

- `VLLM_API_KEY`: API key for authorization
- `VLLM_ALLOW_RUNTIME_LORA_UPDATING`: Enable/disable runtime LoRA updates

## Running the Service

### Using Docker Compose

```bash
docker compose up -d
```

The vLLM API will be available at `http://localhost:8000`.

### Hardware Requirements

- NVIDIA GPU with at least 12GB VRAM
- CUDA 11.8 or higher
- At least 16GB system RAM
