# Wei Cheng (Wayne) Chiu

**LLM Infrastructure · GPU Inference · Solutions Architecture**

Upstream contributions across the LLM-inference stack, paired with production
work that turns deployment requirements into reliable, on-premises GenAI
systems. Focused on model serving, GPU infrastructure, and solution
architecture across Linux, Kubernetes, PyTorch, CUDA, TensorRT-LLM, vLLM, and
Triton.

[Portfolio](https://wayne.is-a.dev/) ·
[PR wall](https://prs.wayne.is-a.dev) ·
[LinkedIn](https://www.linkedin.com/in/wei-cheng-chiu) ·
[CV](https://wayne.is-a.dev/cv.pdf)

## Focus

- **Upstream inference work:** correctness and performance across FlashInfer,
  vLLM, PyTorch, Dynamo, and the surrounding serving stack. The complete live
  record is on [prs.wayne.is-a.dev](https://prs.wayne.is-a.dev).
- **GPU infrastructure:** model serving, distributed communication, quantization,
  and kernel paths across vLLM, TensorRT-LLM, SGLang, Triton, Dynamo, and
  FlashInfer.
- **Solution architecture:** deployment constraints, preflight validation,
  troubleshooting, acceptance, and production handover for on-premises LLM
  systems.

## Representative merged work

| Project | Change |
| --- | --- |
| FlashInfer | [Fixed an SM120/121 multi-CTA radix top-k stream hang](https://github.com/flashinfer-ai/flashinfer/pull/3615) and [NVFP4 attention correction layout](https://github.com/flashinfer-ai/flashinfer/pull/3838) |
| vLLM | [Made tokenizers survive pickling](https://github.com/vllm-project/vllm/pull/45460) and [fixed streaming message metadata](https://github.com/vllm-project/vllm/pull/45376) |
| PyTorch | [Restored the dropped `root` argument in `nccl.broadcast`](https://github.com/pytorch/pytorch/pull/187216) |
| Dynamo | [Cancelled in-flight KV-router recovery when a worker is removed](https://github.com/ai-dynamo/dynamo/pull/10616) and [resolved aggregate planner workers by DGD component type](https://github.com/ai-dynamo/dynamo/pull/11578) |

## Selected projects

| Project | Evidence |
| --- | --- |
| [trtllm-triton-serving](https://github.com/waynehacking8/trtllm-triton-serving) | TensorRT-LLM vs vLLM on H100; 12 controlled studies |
| [tensor-core-from-scratch](https://github.com/waynehacking8/tensor-core-from-scratch) | 10 CUDA matmul kernels from naive to Tensor Cores |
| [inference-kernel-cookbook](https://github.com/waynehacking8/inference-kernel-cookbook) | Flash Attention, KV cache, and paged attention from scratch |
| [nccl-collectives-bench](https://github.com/waynehacking8/nccl-collectives-bench) | NCCL bandwidth, latency, NVLS, and TP-decode limits |
| [nim-agent-blueprint](https://github.com/waynehacking8/nim-agent-blueprint) | NVIDIA NIM agentic RAG with evaluation and observability |
| [llm-security-lab](https://github.com/waynehacking8/llm-security-lab) | Reproducible LLM attacks and defenses |

## Technical writing

- [TensorRT-LLM vs vLLM: the concurrency crossover](https://wayne.is-a.dev/blog/notes-trtllm-triton-serving/)
- [Where tensor-parallel inference hits the NVLink wall](https://wayne.is-a.dev/blog/nccl-nvlink-bandwidth/)
- [The 0% RAG result failed the harder test](https://wayne.is-a.dev/blog/rag-groundedness-guardrail/)
- [From naive GEMM to WMMA](https://wayne.is-a.dev/blog/notes-cuda-tensor-core-gemm/)
