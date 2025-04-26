bench_serving:
	python benchmarks/benchmark_serving.py \
		--model meta-llama/Llama-3.2-1B-Instruct \
		--tokenizer meta-llama/Llama-3.2-1B-Instruct \
		--endpoint /v1/completions \
		--dataset-name sharegpt \
		--dataset-path benchmarks/ShareGPT_V3_unfiltered_cleaned_split.json \
		--request-rate 10.0 \
		--max-concurrency 5 \
		--result-dir ./benchmarks/results --save-result --save-detailed

benchmark_prefix_caching:
    python benchmarks/benchmark_prefix_caching.py \
		--model meta-llama/Llama-3.2-1B-Instruct \
		--tokenizer meta-llama/Llama-3.2-1B-Instruct \
		--dataset-path benchmarks/ShareGPT_V3_unfiltered_cleaned_split.json \
        --enable-prefix-caching \
        --num-prompts 20 \
        --repeat-count 5 \
        --input-length-range 128:256