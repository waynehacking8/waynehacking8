# Wei Cheng (Wayne) Chiu

**Field Application Engineer @ [Taiwan AILabs](https://ailabs.tw/)**

I am a Field Application Engineer targeting customer-facing **AI Solutions
Architect** roles, with hands-on work across **Generative AI (GenAI), LLM
systems, and NVIDIA GPU computing**. I translate customer requirements into
production-ready, on-premises deployments on Linux, Kubernetes, PyTorch, CUDA,
TensorRT-LLM, vLLM, and Triton—from proof of concept (PoC) through
troubleshooting, acceptance, and handover.

[Portfolio](https://wayne.is-a.dev/) ·
[PR wall](https://prs.wayne.is-a.dev) ·
[LinkedIn](https://www.linkedin.com/in/wei-cheng-chiu) ·
[CV](https://wayne.is-a.dev/cv.pdf)

## What I work on

- **AI solutions architecture:** turn customer requirements and site constraints
  into GenAI/LLM deployment plans, acceptance criteria, and production handover.
- **GPU inference:** benchmark and debug serving, communication, quantization, and
  kernel paths across vLLM, TensorRT-LLM, SGLang, Triton, Dynamo, and FlashInfer.
- **Upstream correctness:** 18 merged/landed changes, with the complete live record
  on [prs.wayne.is-a.dev](https://prs.wayne.is-a.dev).

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
