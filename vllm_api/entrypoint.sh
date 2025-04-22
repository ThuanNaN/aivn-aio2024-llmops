#!/bin/bash
set -e

# Find the Python executable
PYTHON_CMD=$(which python3 2>/dev/null || which python 2>/dev/null)
if [ -z "$PYTHON_CMD" ]; then
    echo "Python executable not found! Please install Python."
    exit 1
fi

echo "Using Python executable: $PYTHON_CMD"

# Start vllm in the background
$PYTHON_CMD -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3.2-1B-Instruct \
  --port 8000 \
  --quantization bitsandbytes \
  --gpu-memory-utilization 0.9 \
  --max-model-len 4096 \
  --enable-lora &

# Store the PID of the background process
VLLM_PID=$!

# Function to check if the API is ready
wait_for_api() {
  echo "Waiting for vLLM API to be ready..."
  while ! curl -s -H "Authorization: Bearer $VLLM_API_KEY" http://localhost:8000/v1/models > /dev/null; do
    echo "API not ready yet, waiting..."
    sleep 5
  done
  echo "vLLM API is ready!"
}

# Wait for the API to be ready
wait_for_api

# Run the script to load lora adapters
echo "Loading LoRA adapters..."
export VLLM_API_KEY=$VLLM_API_KEY
bash /app/adapters.sh

# Wait for the vllm process
wait $VLLM_PID
