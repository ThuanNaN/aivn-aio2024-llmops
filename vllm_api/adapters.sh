#!/bin/bash

# Preload/validate paths
MED_QA_LORA_DIR="/root/.cache/huggingface/hub/models--thuanan--med-mcqa-llama-3.2-1B-Instruct-4bit-lora/snapshots/f211dff2cd67765206902672f51fb683854801e8"
VSF_LORA_DIR="/root/.cache/huggingface/hub/models--thuanan--Llama-3.2-1B-Instruct-lora-vsf/snapshots/a4ecdb44c2d665ad5a2cfcbc6f005f3e2e3646cc"

# Curl command to load lora adaptors
curl -X POST "http://localhost:8000/v1/load_lora_adapter" \
    -H "Authorization: Bearer $VLLM_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "medqa-lora",
        "lora_path": "'"$MED_QA_LORA_DIR"'"
    }'

curl -X POST "http://localhost:8000/v1/load_lora_adapter" \
    -H "Authorization: Bearer $VLLM_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
        "lora_name": "vsf-lora",
        "lora_path": "'"$VSF_LORA_DIR"'"
    }'