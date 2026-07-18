<h1 align="center">Hi, I'm Wayne 👋</h1>
<p align="center">A GPU performance engineer based in Taiwan.</p>

<p align="center">
  <a href="https://waynehacking8.github.io/">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/wei-cheng-chiu">LinkedIn</a> ·
  <a href="https://github.com/pulls?q=is%3Apr+author%3Awaynehacking8+archived%3Afalse">My PRs</a> ·
  <a href="https://x.com/WEICHENGCH52824">X / Twitter</a> ·
  <a href="mailto:waynehacking8@gmail.com">Email</a>
</p>

### 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=c,cpp,python,pytorch,linux,bash,git,github,docker,vscode" />
</p>

### 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=waynehacking8&show_icons=true&theme=tokyonight&hide_border=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=waynehacking8&layout=compact&theme=tokyonight&hide_border=true" />
</p>

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=waynehacking8&theme=tokyonight&hide_border=true" />
</p>

### 🐍 Contribution Snake

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/waynehacking8/waynehacking8/output/github-contribution-grid-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/waynehacking8/waynehacking8/output/github-contribution-grid-snake.svg" />
    <img alt="contribution snake animation" src="https://raw.githubusercontent.com/waynehacking8/waynehacking8/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

---

MS Computer Science @ NTUST. I work at the intersection of GPU systems and ML — writing CUDA kernels,
benchmarking inference stacks, and shipping fixes upstream to the LLM-serving ecosystem. My niche:
**early consumer-Blackwell (SM120 / SM121) enablement, validated on a real RTX PRO 6000 96GB** — the kernels and
dispatch paths most repos can't yet test because almost no one has the hardware.

## 🔧 Open-source contributions

Across the LLM-inference stack — **3 merged/landed · 35 in review** — see the live
[**merged-PR feed**](https://github.com/pulls?q=is%3Apr+author%3Awaynehacking8+is%3Amerged+archived%3Afalse).

**Merged / landed in main**

| Project | PR | What it fixes |
| --- | --- | --- |
| **PyTorch** | [#187216](https://github.com/pytorch/pytorch/pull/187216) | `[CUDA][NCCL]` `nccl.broadcast` was dropping its `root` argument — landed in `main` (`c3c33fd`) |
| **vLLM** | [#45460](https://github.com/vllm-project/vllm/pull/45460) | Tokenizer now survives pickling out of `maybe_make_thread_pool` |
| **vLLM** | [#45376](https://github.com/vllm-project/vllm/pull/45376) | Streaming `message_start` event sets `type`/`role` explicitly |

**In review** — selected, grouped by project (counts are live PRs):

| Project | # | Representative work |
| --- | :-: | --- |
| **vLLM** | 10 | NVFP4 MoE per-expert scale validation · FP8 MoE+LoRA routed to Marlin · async-KV-load scheduling fix |
| **SGLang** | 9 | SM120/SM121 dispatch for `int8_scaled_mm` & `fp8_blockwise_scaled_grouped_mm` · SM120 shared-mem-safe attention block size |
| **FlashInfer** | 8 | Multi-CTA radix top-k stream hangs on SM120/121 · NVFP4 global-scale threading through the unified MoE API |
| **NVIDIA TensorRT-LLM** | 3 | CuteDSL MoE ghost-token & global-index fixes · DeepSeek-V2-Lite `e_score_correction_bias` guard |
| **Dynamo** | 3 | KV-router cancels in-flight recovery on worker removal · RTX PRO 6000 Blackwell GPU SKU |
| **torchao** | 2 | PT2E/X86 annotation fallback for reused `nn.Linear`/`nn.Conv2d` with fusable post-ops |

> Most SM120 work above is reproduced and validated on my own RTX PRO 6000 96GB Blackwell box.

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

## Stack

`CUDA` · `Tensor Cores` · `PTX` · `SM120 / Blackwell` · `Python` · `PyTorch` · `TensorRT-LLM` · `vLLM` · `SGLang` ·
`FlashInfer` · `Triton Inference Server` · `NCCL` · `NVFP4 / FP8 quantization` · `Differential Privacy` · `Federated Learning`

---

<p align="center"><sub>
  Also known as Wayne Chiu / 邱偉誠 ·
  <a href="https://waynehacking8.github.io/">waynehacking8.github.io</a>
</sub></p>
