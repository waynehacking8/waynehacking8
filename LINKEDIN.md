# LinkedIn — ready-to-paste assets

Aligned 1:1 with the GitHub profile so SEO keywords stack:
**GPU performance · LLM inference · SM120/Blackwell · upstream contributor (PyTorch/vLLM/SGLang/FlashInfer/TensorRT-LLM).**

---

## 1. Headline  (≤220 chars) — LIVE

```
Machine Learning Engineer | LLM Inference & GPU Performance | CUDA / Tensor-Core kernels on NVIDIA Blackwell | vLLM · TensorRT-LLM | MS CS @ NTUST
```

**Why this shape (the honest version — based on real headlines, not assumptions):**

Two different conventions exist, and which one is right depends on whether you have a brand-name employer:

- **Senior/industry people** write *short* — `function @ company`: "Inference Optimization @ NVIDIA",
  "ML Performance @ Nvidia", "Member of Technical Staff at OpenAI | ex-NVIDIA". No tech-stack list at all —
  the **company name is the credential**, and recruiters hunt them by name.
- **Job-seekers without that brand** (incl. strong MS students) write `Role | focus | tech | degree` —
  because they need to be **found via keyword search**. Copying the seniors' minimalism would make you invisible.

You're in the second group, so the headline is keyword-discoverable on purpose. What it still avoids
(the part that read as junior in the first drafts):
- ❌ contribution counts / status — "Merged into X", "35 PRs in review" reads as a scoreboard, not a person.
- ❌ over-long jargon — keep tech as plain keywords (the niche specifics like SM120 live in About/Experience).

Save the contribution counts (3 merged / 35 in review) for About, Featured and Experience, where context makes them land.

---

## 2. About — first two lines (these are the only part shown before "…see more")

```
I ship fixes upstream to the LLM-inference stack — 3 merged/landed across PyTorch & vLLM,
35 in review across SGLang, FlashInfer, TensorRT-LLM and Dynamo. My niche is early
consumer-Blackwell (SM120) enablement, validated on a real RTX PRO 6000 96GB.
```

Then continue with your existing About body. Keep the keywords CUDA / Tensor Cores / NVFP4 / FP8 in the first paragraph.

---

## 3. Featured  (the only visually-prominent block on LinkedIn — currently underused)

Add these as links (LinkedIn auto-pulls title + thumbnail):

| Pin | URL |
| --- | --- |
| PyTorch — nccl.broadcast root-arg fix (landed in main) | https://github.com/pytorch/pytorch/pull/187216 |
| vLLM — tokenizer-survives-pickling fix (merged) | https://github.com/vllm-project/vllm/pull/45460 |
| GitHub profile (contributions + flagship projects) | https://github.com/waynehacking8 |
| Portfolio | https://waynehacking8.github.io/ |

---

## 4. Experience — new entry

```
Title:        Open-Source Contributor — LLM Inference Stack
Employment:   Self-employed / Open source
Dates:        Jan 2026 – Present
Location:     Remote
```

Bullets:
```
• Ship kernel & correctness fixes upstream to the LLM-serving ecosystem — 3 merged/landed
  (PyTorch, vLLM) and 35 in review across SGLang, FlashInfer, NVIDIA TensorRT-LLM, Dynamo, torchao.
• Specialise in consumer-Blackwell (SM120/SM121) enablement on a real RTX PRO 6000 96GB:
  int8/FP8 GEMM dispatch, NVFP4 MoE scale handling, shared-memory-safe attention block sizing,
  and multi-CTA top-k stream-hang fixes.
• PyTorch [CUDA][NCCL]: found and fixed nccl.broadcast silently dropping its root argument
  (landed in main, commit c3c33fd).
• vLLM: tokenizer pickling survival, NVFP4 MoE per-expert scale validation, FP8 MoE+LoRA
  routing to Marlin kernels.
```

---

## 5. Skills to add (so the headline keywords are also searchable as Skills)

```
CUDA · GPU Kernels · Tensor Cores · PTX · NVIDIA Blackwell (SM120) · vLLM · SGLang ·
TensorRT-LLM · FlashInfer · PyTorch · LLM Inference · Model Quantization (NVFP4 / FP8) · NCCL
```

---

## 6. Post drafts  (publish when YOU choose — these broadcast to your whole network)

### Post A — PyTorch merge (highest-credibility hook)

```
A fix I sent to PyTorch core just landed in main 🎉

[CUDA][NCCL] nccl.broadcast was silently dropping its `root` argument — so a broadcast
meant to originate from rank N could originate from the wrong rank. Small diff, nasty
class of bug: it only shows up in multi-GPU collectives and fails quietly.

PR #187216 → https://github.com/pytorch/pytorch/pull/187216

It's part of a wider push — I currently have 35 more PRs in review across vLLM, SGLang,
FlashInfer and TensorRT-LLM, a lot of it early consumer-Blackwell (SM120) enablement
validated on a real RTX PRO 6000.

#CUDA #PyTorch #GPU #LLM #Blackwell
```

### Post B — the SM120 niche (differentiation)

```
Most LLM-serving repos can't test consumer-Blackwell (SM120 / RTX PRO 6000) kernels —
almost nobody on the contributor side has the card. I do, so I've been filling that gap:

• SGLang — SM120/SM121 dispatch for int8_scaled_mm and fp8_blockwise grouped GEMM
• FlashInfer — fixed multi-CTA radix top-k stream hangs on SM120/121
• Dynamo — added the RTX PRO 6000 Blackwell GPU SKU
• vLLM — NVFP4 MoE per-expert scale validation

35 PRs in review, 3 merged so far. Every SM120 change reproduced on real hardware.

If you work on inference and hit a Blackwell-only kernel bug, ping me.

#GPU #CUDA #Blackwell #LLMInference #vLLM #SGLang
```

---

### Consistency checklist
- [ ] Headline, GitHub hero, and Featured all say the same niche phrase ("consumer-Blackwell / SM120 / RTX PRO 6000").
- [ ] Same project names spelled identically everywhere (vLLM, SGLang, FlashInfer, TensorRT-LLM).
- [ ] GitHub link in Contact info + Featured + About.
