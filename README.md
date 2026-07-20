### Hi I'm Wayne 

**Open Source GPU Performance Engineer** <br>**Field Application Engineer @ Taiwan AILabs**

[wayne.is-a.dev](https://wayne.is-a.dev/) ·
[PR wall](https://prs.wayne.is-a.dev) ·
[LinkedIn](https://www.linkedin.com/in/wei-cheng-chiu) ·
[X @itswaynechiu](https://x.com/itswaynechiu)

##  Tech stack

**GPU & kernels**<br>
![CUDA](https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white)
![CUTLASS](https://img.shields.io/badge/CUTLASS-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Tensor Cores / PTX](https://img.shields.io/badge/Tensor_Cores_%2F_PTX-44566c?style=flat-square)
![NVFP4 / FP8](https://img.shields.io/badge/NVFP4_%2F_FP8_quantization-44566c?style=flat-square)

**Inference serving**<br>
![vLLM](https://img.shields.io/badge/vLLM-3268b0?style=flat-square)
![SGLang](https://img.shields.io/badge/SGLang-d1531f?style=flat-square)
![FlashInfer](https://img.shields.io/badge/FlashInfer-7d5bd0?style=flat-square)
![TensorRT-LLM](https://img.shields.io/badge/TensorRT--LLM-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Dynamo](https://img.shields.io/badge/Dynamo-76B900?style=flat-square&logo=nvidia&logoColor=white)
![NCCL](https://img.shields.io/badge/NCCL-76B900?style=flat-square&logo=nvidia&logoColor=white)
![Triton Inference Server](https://img.shields.io/badge/Triton_Inference_Server-76B900?style=flat-square&logo=nvidia&logoColor=white)

**Languages & ML**<br>
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C/C++](https://img.shields.io/badge/C%2FC%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![Federated Learning / DP](https://img.shields.io/badge/Federated_Learning_%2F_DP-57810a?style=flat-square)

**Systems**<br>
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat-square&logo=cmake&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

###  Tools I use

![Neovim](https://img.shields.io/badge/Neovim-57A143?style=flat-square&logo=neovim&logoColor=white)
![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=claude&logoColor=white)
![Obsidian](https://img.shields.io/badge/Obsidian-7C3AED?style=flat-square&logo=obsidian&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Tailscale](https://img.shields.io/badge/Tailscale-242424?style=flat-square&logo=tailscale&logoColor=white)
![Nsight](https://img.shields.io/badge/Nsight_Compute_%2F_Systems-76B900?style=flat-square&logo=nvidia&logoColor=white)

###  Contribution

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/waynehacking8/waynehacking8/output/github-contribution-grid-snake-dark.svg?v=snk">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/waynehacking8/waynehacking8/output/github-contribution-grid-snake.svg?v=snk">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/waynehacking8/waynehacking8/output/github-contribution-grid-snake.svg?v=snk">
</picture>

###  Latest Posts

- [Notes — TensorRT-LLM + Triton serving](https://wayne.is-a.dev/blog/notes-trtllm-triton-serving/)
- [Tensor-parallel & the NVLink wall](https://wayne.is-a.dev/blog/nccl-nvlink-bandwidth/)
- [RAG groundedness: 0% vs 50%](https://wayne.is-a.dev/blog/rag-groundedness-guardrail/)
- [Notes — CUDA Tensor Core GEMM (WMMA)](https://wayne.is-a.dev/blog/notes-cuda-tensor-core-gemm/)

---

 I work at the intersection of GPU systems and ML — writing CUDA kernels,
benchmarking inference stacks, and shipping fixes upstream to the LLM-serving ecosystem. My niche:
**early consumer-Blackwell (SM120 / SM121) enablement, validated on real Blackwell workstation hardware** — the kernels and
dispatch paths most repos can't yet test because almost no one has the hardware.

##  Open-source contributions

Across the LLM-inference stack — **17 merged/landed · 60 in review** — see the live
[**PR wall → prs.wayne.is-a.dev**](https://prs.wayne.is-a.dev) (auto-updating, with [RSS](https://prs.wayne.is-a.dev/feed.xml)).

**Merged / landed in main**

| Project | # | Representative merged work |
| --- | :-: | --- |
| **FlashInfer** | 7 | [SM120/121 multi-CTA radix top-k stream hang](https://github.com/flashinfer-ai/flashinfer/pull/3615) · [SM120 NVFP4 attention qk-correction layout / row-sum / lse](https://github.com/flashinfer-ai/flashinfer/pull/3838) · [MXFP8-aware MoE gemm profiler](https://github.com/flashinfer-ai/flashinfer/pull/3614) |
| **vLLM** | 3 | [Tokenizer survives pickling](https://github.com/vllm-project/vllm/pull/45460) · [streaming `message_start` sets `type`/`role`](https://github.com/vllm-project/vllm/pull/45376) · [clear error for structured outputs on diffusion decoders](https://github.com/vllm-project/vllm/pull/45468) |
| **LMDeploy** | 3 | [InternVL LoRA loading TypeError](https://github.com/InternLM/lmdeploy/pull/4684) · [double-counted `max_q_seqlen` in decode delta](https://github.com/InternLM/lmdeploy/pull/4685) · [builtin chat-template ImportError](https://github.com/InternLM/lmdeploy/pull/4690) |
| **PyTorch** | 1 | [`nccl.broadcast` was dropping its `root` argument](https://github.com/pytorch/pytorch/pull/187216) — landed in `main` (`c3c33fd`) |
| **Dynamo** | 1 | [KV-router cancels in-flight recovery on worker removal](https://github.com/ai-dynamo/dynamo/pull/10616) |
| **compressed-tensors** | 1 | [Skip device-map entries with no local module in dispatch](https://github.com/vllm-project/compressed-tensors/pull/737) |
| **torchao** | 1 | [PT2E/X86 plain-linear annotation fallback for reused `nn.Linear`](https://github.com/pytorch/ao/pull/4480) |

**In review** — grouped by project (counts as of 2026-07-18):

| Project | # | Representative work |
| --- | :-: | --- |
| **SGLang** | 17 | SM120/SM121 dispatch for `int8_scaled_mm` & `fp8_blockwise_scaled_grouped_mm` · SM120 shared-mem-safe attention block size |
| **vLLM** | 15 | NVFP4 MoE per-expert scale validation · FP8 MoE+LoRA routed to Marlin · async-KV-load scheduling fix |
| **FlashInfer** | 13 | NVFP4 global-scale threading through the unified MoE API · cuDNN full-sequence Q batch stride in batch prefill |
| **Dynamo** | 5 | Blackwell workstation GPU SKU support · KV-router hardening follow-ups |
| **NVIDIA TensorRT-LLM** | 4 | CuteDSL MoE ghost-token & global-index fixes · DeepSeek-V2-Lite `e_score_correction_bias` guard |
| **NVIDIA CUTLASS** | 4 | SM120 grouped NVFP4 block-scaled GEMM in `cutlass_library` · CuTeDSL sub-byte `make_ptr` / `is_major` / uint-lowering fixes |
| **torchao** | 1 | Reused-module fallback extended to `nn.Conv2d` (follow-up to merged #4480) |
| **LMCache** | 1 | Clear `reqs_status` on async-lookup timeout to prevent recall KeyError |

> Most SM120 work above is reproduced and validated on real Blackwell workstation hardware.

## 🚀 Flagship projects

| Project | What it is | Key number |
| --- | --- | --- |
| **[tensor-core-from-scratch](https://github.com/waynehacking8/tensor-core-from-scratch)** | 10 progressive CUDA matmul kernels from naive to tensor cores on Blackwell. | 100 TFLOPS (34% of cuBLAS HGEMM) |
| **[inference-kernel-cookbook](https://github.com/waynehacking8/inference-kernel-cookbook)** | LLM inference techniques from scratch — Flash Attention, KV Cache, Paged Attention. | 81× speedup, 1000× memory reduction |
| **[trtllm-triton-serving](https://github.com/waynehacking8/trtllm-triton-serving)** | TensorRT-LLM vs vLLM head-to-head on H100 — 12 studies reproducing NVIDIA's 27.7k tok/s. | 100.3% of published benchmark |
| **[nccl-collectives-bench](https://github.com/waynehacking8/nccl-collectives-bench)** | NCCL collective benchmarks on 8×H100 NVSwitch — bandwidth, latency, NVLS, TP-decode ceiling. | 365 GB/s (77% NVLink budget) |
| **[llm-security-lab](https://github.com/waynehacking8/llm-security-lab)** | LLM security from first principles — prompt extraction, injection, model stealing. Attack + defense. | 19 leaks → 2 with defense |

## Other work

| Project | What it is |
| --- | --- |
| **[blackwell-tensorcore-kernels](https://github.com/waynehacking8/blackwell-tensorcore-kernels)** | Hand-written CUDA Tensor Core GEMM kernels on Blackwell (sm_120) and Hopper (sm_90). |
| **[federated-learning-lab](https://github.com/waynehacking8/federated-learning-lab)** | From-scratch FL: FedAvg / FedProx / SCAFFOLD / FedLoRA, DP-SGD & secure aggregation. 33/33 tests. |
| **[nim-agent-blueprint](https://github.com/waynehacking8/nim-agent-blueprint)** | Agentic RAG on NVIDIA NIM — hallucination evaluation on adversarial SQuAD 2.0 (N=200). |
| **[physgate](https://github.com/waynehacking8/physgate)** | Validate LLM-generated robot plans in GPU physics simulation (Isaac Lab + ROS2 + MCP). |

## Research

- **SelGrad** — selective-gradient defense for privacy-preserving ML. Under review, *IEEE TDSC*.
- Federated learning & differential privacy — robustness and personalization under Non-IID data.

---

<p align="center"><sub>
  Also known as Wayne Chiu / 邱偉誠 ·
  <a href="https://wayne.is-a.dev/">wayne.is-a.dev</a> ·
  <a href="https://www.linkedin.com/in/wei-cheng-chiu">LinkedIn</a> ·
  <a href="https://prs.wayne.is-a.dev">My PRs</a> ·
  <a href="https://x.com/itswaynechiu">X</a> ·
  <a href="mailto:waynehacking8@gmail.com">Email</a>
</sub></p>

