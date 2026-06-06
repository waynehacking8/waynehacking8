<h1 align="center">Wei Cheng (Wayne) Chiu &nbsp;·&nbsp; 邱偉誠</h1>

<p align="center">
  <b>GPU Performance Engineer &amp; AI Systems Builder</b><br>
  CUDA kernel optimization, LLM inference, multi-GPU serving, AI security, privacy-preserving ML.
</p>

<p align="center">
  <a href="https://waynehacking8.github.io/">Portfolio</a> ·
  <a href="https://www.linkedin.com/in/wei-cheng-chiu">LinkedIn</a> ·
  <a href="https://x.com/WEICHENGCH52824">X / Twitter</a> ·
  <a href="mailto:waynehacking8@gmail.com">Email</a>
</p>

---

MS Computer Science @ NTUST. I work at the intersection of GPU systems and ML — writing CUDA kernels, benchmarking inference stacks, and building production AI systems on the NVIDIA platform.

## Flagship projects

| Project | What it is | Key number |
| --- | --- | --- |
| **[tensor-core-from-scratch](https://github.com/waynehacking8/tensor-core-from-scratch)** | 10 progressive CUDA matmul kernels from naive to tensor cores on Blackwell. | 100 TFLOPS (34% of cuBLAS HGEMM) |
| **[inference-kernel-cookbook](https://github.com/waynehacking8/inference-kernel-cookbook)** | LLM inference techniques from scratch — Flash Attention, KV Cache, Paged Attention. | 81x speedup, 1000x memory reduction |
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

`CUDA` · `Tensor Cores` · `PTX` · `Python` · `PyTorch` · `TensorRT-LLM` · `Triton Inference Server` · `NCCL` ·
`vLLM` · `NVIDIA NIM` · `LangGraph` · `Docker` · `Differential Privacy` · `Federated Learning`

---

<p align="center"><sub>
  Also known as Wayne Chiu / 邱偉誠 ·
  <a href="https://waynehacking8.github.io/">waynehacking8.github.io</a>
</sub></p>
