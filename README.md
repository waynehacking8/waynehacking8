# Wayne Chiu

**Open-source GPU performance engineer · Field Application Engineer at Taiwan AI Labs**

I work where GPU kernels meet production LLM serving: reproducing failures on real
hardware, fixing the lowest responsible layer, and carrying those fixes upstream.
My current niche is early consumer-Blackwell (`SM120` / `SM121`) enablement.

[Portfolio](https://wayne.is-a.dev/) ·
[Live PR wall](https://prs.wayne.is-a.dev/) ·
[CV](https://wayne.is-a.dev/cv.pdf) ·
[LinkedIn](https://www.linkedin.com/in/wei-cheng-chiu) ·
[X](https://x.com/itswaynechiu) ·
[Email](mailto:waynehacking8@gmail.com)

| Upstream impact | Hardware access | Focus |
| :---: | :---: | :---: |
| **17 merged / landed · 60 in review** | **Blackwell workstation · 8×H100 NVSwitch** | **CUDA kernels · inference serving · correctness** |

> Making every FLOP count — without losing the right answer.

## Selected upstream impact

| Project | Landed work | Current work in review |
| --- | --- | --- |
| **FlashInfer** | 7 fixes: SM120/121 top-k hang, NVFP4 attention layout/correction, MXFP8 MoE profiling | NVFP4 unified-MoE plumbing, cuDNN prefill strides, SM120 kernels |
| **vLLM** | 3 fixes: tokenizer pickling, streaming message metadata, structured-output validation | NVFP4/FP8 MoE, LoRA routing, async KV scheduling |
| **LMDeploy** | 3 fixes: InternVL LoRA loading, decode delta accounting, chat-template import | Serving correctness follow-ups |
| **PyTorch / torchao** | NCCL broadcast root fix; PT2E/X86 reused-linear fallback | Reused-module convolution fallback |
| **NVIDIA Dynamo** | KV-router recovery cancellation fix | Blackwell workstation support and router hardening |
| **TensorRT-LLM / CUTLASS** | — | CuteDSL MoE correctness and SM120 grouped NVFP4 GEMM enablement |

The [live PR wall](https://prs.wayne.is-a.dev/) is the source of truth for current
status, repository links, timestamps, and an [RSS feed](https://prs.wayne.is-a.dev/feed.xml).

## Flagship work

| Project | What it proves | Measured result |
| --- | --- | --- |
| [**tensor-core-from-scratch**](https://github.com/waynehacking8/tensor-core-from-scratch) | Ten progressive CUDA matmul kernels, from naive code to Tensor Cores on Blackwell | **100 TFLOPS**, 34% of cuBLAS HGEMM |
| [**inference-kernel-cookbook**](https://github.com/waynehacking8/inference-kernel-cookbook) | Flash Attention, KV cache, and paged attention built from first principles | **81× speedup**, **1000× memory reduction** |
| [**trtllm-triton-serving**](https://github.com/waynehacking8/trtllm-triton-serving) | Controlled TensorRT-LLM vs vLLM study on H100 | Reproduced **100.3%** of NVIDIA's published throughput |
| [**nccl-collectives-bench**](https://github.com/waynehacking8/nccl-collectives-bench) | Collective bandwidth, latency floors, NVLS, and TP decode ceiling on 8×H100 | **365 GB/s**, 77% of NVLink budget |
| [**blackwell-tensorcore-kernels**](https://github.com/waynehacking8/blackwell-tensorcore-kernels) | Hand-written Tensor Core kernels across Blackwell and Hopper | Raw `mma.sync` reaches **106%** of cuBLAS-TC on SM120 |
| [**nim-agent-blueprint**](https://github.com/waynehacking8/nim-agent-blueprint) | Adversarial RAG grounding evaluation with paired statistical tests | Nine gate methods, **N=200** |

## Working stack

`CUDA` · `CUTLASS` · `PTX` · `NVFP4 / FP8` · `FlashInfer` · `vLLM` · `SGLang` ·
`TensorRT-LLM` · `Dynamo` · `NCCL` · `Triton` · `PyTorch` · `C++` · `Python` ·
`Linux` · `Docker` · `Kubernetes` · `Nsight Compute / Systems`

## Research and writing

- **SelGrad** — selective-gradient defense for safety alignment under harmful fine-tuning; under review at *IEEE TDSC*.
- [TensorRT-LLM + Triton serving notes](https://wayne.is-a.dev/blog/notes-trtllm-triton-serving/)
- [Tensor parallelism and the NVLink wall](https://wayne.is-a.dev/blog/nccl-nvlink-bandwidth/)
- [RAG groundedness: 0% vs 50%](https://wayne.is-a.dev/blog/rag-groundedness-guardrail/)
- [CUDA Tensor Core GEMM notes](https://wayne.is-a.dev/blog/notes-cuda-tensor-core-gemm/)

<p align="center"><sub>
Wei-Cheng (Wayne) Chiu · 邱偉誠 · Taipei, Taiwan · UTC+8
</sub></p>
