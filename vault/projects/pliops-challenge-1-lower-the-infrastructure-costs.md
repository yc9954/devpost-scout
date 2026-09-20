---
slug: "pliops-challenge-1-lower-the-infrastructure-costs"
url: "https://devpost.com/software/pliops-challenge-1-lower-the-infrastructure-costs"
title: "Pliops Challenge #1 - Lower the infrastructure Costs"
hackathon: "DeveloperWeek 2025 Hackathon"
organization: "DevNetwork"
winner: true
words: 361
team_size: 0
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/structured_db"
---

# Pliops Challenge #1 - Lower the infrastructure Costs

> Provide solution for Pliops Challenge #1

[Devpost](https://devpost.com/software/pliops-challenge-1-lower-the-infrastructure-costs) · hackathon [[DeveloperWeek 2025 Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[structured_db]]

**stack** llm, python

## How they structured the write-up

- 1. when using llm inferencing, specifically vllm as a framework, how would you be able to reduce the number of gpus used for prefill (or decode) operations?
- 2. is caching prompts the only way?
- 3. can the kvcaches be preserved at the hardware level close to the gpu?

## Body

1. When using LLM Inferencing, specifically vLLM as a framework, how would you be able to reduce the number of GPUs used for Prefill (or decode) operations? When working with vLLM for LLM inference, there are several strategies to reduce GPU usage during prefill/decode operations: Optimize Batch Processing: Implement dynamic batching to combine multiple requests Adjust sequence lengths to maximize GPU utilization Use continuous batching to reduce memory fragmentation Memory Management Techniques: from vllm import LLMEngine, SamplingParams engine_params = { "tensor_parallel_size": 1, # Reduce if using multiple GPUs "max_num_batched_tokens": 2048, # Adjust based on your needs "max_num_seqs": 256, "gpu_memory_utilization": 0.85 # Balance between performance and memory usage } engine = LLMEngine( model="your-model", **engine_params ) 2. Is caching prompts the only way? Prompt caching is not the only way to optimize and make LLM applications more efficient. Some methods are: Prompt Engineering Optimization: Writing more concise and focused prompts Using few-shot learning effectively Removing unnecessary context or redundant information Response Streaming: Implementing streaming responses instead of waiting for complete responses Improving perceived performance for users Client-side Caching: Caching common responses locally Implementing a response cache for frequently asked questions Vector Databases: Using vector embeddings to store and retrieve similar content Implementing semantic search for faster retrieval Fine-tuning: Training models on specific domains Creating smaller, specialized models for specific tasks Request Queue Management: Implementing rate limiting Using job queues for non-real-time responses 3. Can the KVcaches be preserved at the Hardware level close to the GPU? Yes, KV (Key-Value) caches can be preserved at the hardware level close to the GPU, and this is an important optimization technique. GPU Memory Hierarchy for KV Caches: L1 Cache: Closest to GPU cores, fastest access L2 Cache: Shared cache, larger but slightly slower GPU VRAM: Main GPU memory System RAM: Accessible but with higher latency Optimization Techniques __global__ void kv_cache_kernel(float* keys, float* values, int stride) { int idx = blockIdx.x * blockDim.x + threadIdx.x; // Ensure coalesced memory access float key = keys[idx * stride]; float value = values[idx * stride]; // Process data } Performance Impact: Reduced global memory access Lower latency for repeated queries Better utilization of memory bandwidth Improved throughput for inference <div