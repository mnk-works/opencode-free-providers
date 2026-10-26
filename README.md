# opencode-free-providers

**Which AI providers in OpenCode have a free tier?**

OpenCode v2.1.4 ships a provider list built from [models.dev](https://models.dev). This repo snapshots that list, checks every provider for free API access (free tier, free model variants, recurring credits or trial credits), and records what is free **out of the box** - i.e. without an API key or a credit card.

- **237 providers / integrations** exist in the OpenCode provider picker.
- **12** of them already had models enabled by default (the rest need `/connect` first).
- **46 `$0` models** were enabled with zero setup, from 9 providers.
- Only a handful of providers are **genuinely free in a way you can rely on for coding**: OpenCode's own free models, Google AI Studio (Flash tiers), OpenRouter `:free`, UnoRouter `:free`, Kilo Auto Free, NVIDIA's trial endpoints, plus a few Chinese-platform signup quotas.

> Verified **2026-10-26** against OpenCode v2.1.4, `https://models.dev/api.json`, and each vendor's public pricing/docs page. Free tiers change weekly - treat this as a starting point, not a contract. See [Freshness](#freshness-and-caveats).

---

## TL;DR - free options ranked for coding agents

| Rank | Provider | What you get free | Catch |
| :--: | :-- | :-- | :-- |
| 1 | **OpenCode Console (`opencode`)** | 9 free models with **no key**: `deepseek-v4.1-flash-free`, `glm-5.3-flash-free`, `mimo-v2.6-flash-free`, `nemotron-3.5-super-vl-free`, `nemotron-3.5-lightning-free`, `nemotron-3-ultra-free`, `beam-free`, `flint-40b-free`, `big-pickle` | "Limited time" models; US/EU hosted; rate-limited |
| 2 | **Google (Gemini API)** | Free-tier tokens on Gemini **3.8 Flash / 3.6 Flash / Flash-Lite**, Gemma 4 | Data may be used to improve Google products; lower RPM/TPM/RPD; no free Gemini 4 Argon |
| 3 | **OpenRouter** | Any model ending in `:free` (21 enabled here) | 50 free requests/day (< $10 lifetime top-up), 1,000/day after |
| 4 | **UnoRouter** | `:free` variants (DeepSeek V4.1 Flash, MiniMax M3.1, Step 5, MiMo V2.6, Nemotron ...) | ~1 request/min/model; Discord rewards instead of a cash trial |
| 5 | **Kilo Gateway** | "Kilo Auto Free" tier, 22 `$0` catalog entries | Rolling/daily limits; paid models at provider cost |
| 6 | **NVIDIA Build** | 52 catalog models at `$0` (DeepSeek V4.1 Flash, GPT-OSS, GLM-5.3, Nemotron) | Trial-only: logged, rate-limited, no confidential data |
| 7 | **Alibaba Model Studio (Bailian)** | Per-model free quota (≈1M tokens, 90 days) | Must activate in Singapore/China region; no Token/Coding Plan key |
| 8 | **ModelScope / SiliconFlow (CN) / Z.AI** | Free daily calls (ModelScope), free GLM Flash models (Z.AI), `$1` credit (SiliconFlow intl) | Region, real-name verification and changing quotas |
| - | **Local (Ollama / LM Studio / Atomic Chat)** | Free forever - your hardware | Not hosted |

Everything else is pay-as-you-go, a paid subscription (OpenCode Go, MiniMax Token Plan, Kimi For Coding, Z.AI Coding Plan, Step Plan, Xiaomi Token Plan, Tencent ...), a cloud account (Azure, Bedrock, Vertex, Databricks, Snowflake, SAP, watsonx, OCI), or a one-off signup credit that is easy to miss.

---

## How this list was produced

1. Started a private OpenCode server in tmux: `opencode serve --hostname 127.0.0.1 --port 4097` (it prints a password; v2 requires basic auth `opencode:<password>`).
2. Pulled the real provider list from the API:
   - `GET /api/integration` → 237 integrations, their auth methods (`key` / `env` / `oauth` / `external` / cloud command) and env var names.
   - `GET /api/model` → 1,262 model entries enabled by default, with `cost` per model.
3. Cross-referenced every provider ID with `https://models.dev/api.json` (the catalog OpenCode builds on) for catalog endpoint, runtime package and `$0` models.
4. Probed every provider's homepage (HTTP status + "free tier / free plan / free trial / no credit card / 免费" phrases) to catch marketing claims, then read the pricing/docs page for anything that looked promising.
5. Recorded each provider in `data/providers.csv` with an **evidence status**:
   - `verified` - confirmed on the vendor's own pricing/docs page
   - `partial` / `claimed` / `listed` - marketing claim or `$0` catalog entry that is not documented as free-to-call
   - `unverified` / `not checked` - no public free offer found; treated as paid

Convenience files:

- `data/providers.csv` - all 237 providers (endpoint, auth, model counts, free status, how to get free, limits, evidence URL).
- `data/enabled-free-models.csv` - the `$0` models enabled by default in the default OpenCode setup.
- The free-model list per provider also lives in the tables below.

To refresh: re-run steps 1-2 (see [Reproduce](#reproduce)), re-fetch `models.dev/api.json`, and update the vendor rows that changed.

---

## Providers enabled by default in OpenCode

These are the providers that already had models in `/models` without running `/connect`. All but `gate` come from models.dev; `gate` was added manually in the OpenCode config.

| Provider | API style / auth | Models | `$0` models | Free? | Notes |
| :-- | :-- | --: | --: | :--: | :-- |
| **OpenCode Console** (`opencode`) | OpenAI-compatible, key/env/OAuth | 9 enabled (130 catalog) | **9** | **yes** | The free models below. Paid Console models are PAYG. |
| **Google** (`google`) | Gemini native, key | 32 | 4 | **yes** | Free tier covers Gemini 3.8 Flash & Flash-Lite, Gemma 4; Argon/Pro paid-only |
| **OpenRouter** (`openrouter`) | OpenRouter native, key | 371 | 21 | **yes** | `:free` variants, 50 req/day (1,000 after $10 top-up) |
| **Hugging Face** (`huggingface`) | OpenAI-compatible, key | 81 | 1 | partial | `zai-org/GLM-4.7-Flash` is $0; PRO gives $2/mo credits |
| **SiliconFlow** (`siliconflow`) | OpenAI-compatible, key | 54 | 0 | partial | `$1` signup credit (intl) |
| **Charm Hyper** (`hyper`) | OpenAI-compatible, key | 23 | 0 | partial | Free trial was a monthly Hypercredit allowance (retired); now PAYG from $5 or $10-$200/mo weekly-credit plans |
| **Mistral** (`mistral`) | Mistral native, key | 19 | 0 | partial | Free chat plan ≠ free API; "Experiment" tier rate-limited |
| **NanoGPT** (`nano-gpt`) | OpenAI-compatible, key | 641 | 4 | partial | PAYG only; `$0` helper routes are not a free plan |
| **DeepSeek** (`deepseek`) | OpenAI-compatible, key | 2 | 0 | no | Off-peak 50% discount only |
| **MiniMax** (`minimax`) | Anthropic-compatible, key | 2 | 0 | no | M3 has a permanent 50% discount |
| **Xiaomi** (`xiaomi`) | OpenAI-compatible, key | 3 | 0 | partial | Welcome bonus credits |
| **Constellation Gate** (`gate`) | Custom OpenAI-compatible | 2 | 2 | partial | User-configured provider, not in models.dev; marketing says "free tier, no card" |

### The 9 free models in OpenCode (`opencode/*`)

| Model ID | Notes |
| :-- | :-- |
| `opencode/deepseek-v4.1-flash-free` | Zero-retention provider per OpenCode docs |
| `opencode/glm-5.3-flash-free` | Zero-retention provider per OpenCode docs |
| `opencode/beam-free` | Retained 30 days for safety; region-blocked in many countries |
| `opencode/mimo-v2.6-flash-free` | Feedback-collection model |
| `opencode/nemotron-3.5-super-vl-free` | NVIDIA trial endpoints - data logged |
| `opencode/nemotron-3.5-lightning-free` | NVIDIA trial endpoints |
| `opencode/nemotron-3-ultra-free` | NVIDIA trial endpoints |
| `opencode/flint-40b-free` | Feedback-collection model |
| `opencode/big-pickle` | Stealth model, free "for a limited time" |

Hide them with `OPENCODE_DISABLE_FREE_MODELS=1` ([docs](https://opencode.ai/v2/docs/console/models/#free-models)).

---

## Top free tier / free plan providers (full evaluation)

These are the providers where the vendor itself documents a free path. Descriptions are from the vendor page (or a strong indication in the catalog), not guesses.

### Hosted LLMs with a real free tier

| Provider | Free offer | Source |
| :-- | :-- | :-- |
| **OpenCode Console** (`opencode`) | 9 free chat models, no key required; no published quota; US/EU hosted | [docs](https://opencode.ai/v2/docs/console/models/) |
| **Google** (`google`) | AI Studio free tier: Gemini 3.8 Flash, 3.6 Flash, 3.1/3.5 Flash-Lite free tokens; Gemma 4 free; data used to improve products on free tier; 5,000 free Search-grounding requests/mo on paid tier | [pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| **OpenRouter** (`openrouter`) | `:free` model variants; 20 req/min, 50 req/day (< $10 lifetime credits) or 1,000/day; negative balance blocks free models | [limits](https://openrouter.ai/docs/api-reference/limits) |
| **UnoRouter** (`unorouter`) | 130+ `:free` models aggregated from ~50 upstreams; ~1 req/min/model; Discord rewards for balance (expire in 12 months) | [docs](https://unorouter.com/en/docs/platform/models-and-pricing) |
| **Kilo Gateway** (`kilo`) | "Start with Kilo Auto Free - no credit card"; 22 `$0` catalog entries | [kilo.ai](https://kilo.ai/) |
| **NVIDIA Build** (`nvidia`) | Trial endpoints, 52 models at `$0` (DeepSeek V4.1 Flash, GPT-OSS, GLM-5.3, Nemotron); requests logged; trial terms | [build.nvidia.com](https://build.nvidia.com/) |
| **Cloudflare Workers AI** (`cloudflare-workers-ai`) | 10,000 Neurons/day free with any Cloudflare account | [docs](https://developers.cloudflare.com/workers-ai/) |
| **Alibaba Model Studio** (`alibaba`, `alibaba-cn`) | New-user free quota per model (typically 1M tokens, 90 days, Singapore region) | [docs](https://www.alibabacloud.com/help/en/model-studio/new-free-quota), [Bailian](https://help.aliyun.com/zh/model-studio/new-free-quota) |
| **ModelScope** (`modelscope`) | Free API calls after binding Alibaba Cloud account; 7 `$0` models | [modelscope.cn](https://modelscope.cn/) |
| **Z.AI / Zhipu AI** (`zai`, `zhipuai`) | Free GLM flash models: `glm-4.5-flash`, `glm-4.7-flash`, `glm-4.6v-flash` | [z.ai/model-api](https://z.ai/model-api) |
| **Groq** (`groq`) | Free developer tier with rate limits (open models, Whisper) | [console.groq.com](https://console.groq.com/) |
| **Cerebras** (`cerebras`) | Free tier with daily token caps | [cloud.cerebras.ai](https://cloud.cerebras.ai/) |
| **Cohere** (`cohere`) | Trial key (rate-limited, non-commercial) | [cohere.com](https://cohere.com/) |
| **GitHub Copilot** (`github-copilot`) | Copilot Free exists; OpenCode connects via device OAuth | [OpenCode docs](https://opencode.ai/v2/docs/providers/) |
| **SiliconFlow CN** (`siliconflow-cn`) | Historically free models (Qwen3-8B, DeepSeek-OCR) + giveaways | [cloud.siliconflow.cn](https://cloud.siliconflow.cn/) |
| **Qiniu** (`qiniu-ai`) | New-user free tokens after real-name signup | [qiniu.com](https://www.qiniu.com/) |

### Signup / trial credits (one-off, not a tier)

| Provider | Offer |
| :-- | :-- |
| **Baseten** | $30 trial credit |
| **Vultr** | $250 / 30-day promo credit |
| **Hugging Face** | PRO: $2/month inference credits (free users: none) |
| **Charm Hyper** | Free monthly Hypercredit allowance was retired; PAYG prepaid credits from $5 |
| **SiliconFlow (intl)** | $1 signup credit |
| **Xiaomi MiMo** | Welcome bonus credits |
| **Jiekou.AI, OrcaRouter, Meganova, AIHubMix** | Small credits / free-listed routes, not documented |
| **Snowflake, Databricks, SAP AI Core, watsonx, OCI** | Cloud-trial credits usable for inference |
| **Perplexity** | $5/month API credit with a Pro subscription |
| **Moonshot, Novita, Fireworks, Together, DeepInfra, Nebius** | Small trial credits, historically |
| **Cloudflare, SambaNova, Groq, Cerebras, Cohere, GitLab, GitHub Copilot** | Ongoing free tiers with caps - see the tables above |

### Local runtimes - free forever

| Provider | Why it counts |
| :-- | :-- |
| **Ollama** (`ollama`) | Local models discovered automatically |
| **LM Studio** (`lmstudio`) | `http://127.0.0.1:1234/v1` |
| **Atomic Chat** (`atomic-chat`) | `http://127.0.0.1:1337/v1` |
| **vLLM** | Any OpenAI-compatible local server (custom provider) |

---

## All 237 providers

`Free?` legend: **yes** = documented free tier/models · **partial** = free models or one-off/trial credit · **no** = paid · **local** = your own hardware · **claimed/listed** = vendor marketing or `$0` catalog entry only · **not checked** = no free offer found on the provider's site, treated as paid.

<details open>
<summary><strong>Show all providers</strong></summary>

| Provider | API style / auth | Models in OpenCode catalog | $0 models | Free? | Best free path |
| --- | --- | ---: | ---: | :--: | --- |
| **302.AI** (`302ai`) | key/env | 125 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Abacus** (`abacus`) | key/env | 108 | — | partial | RouteLLM API has a Free Tier plan; ChatLLM Teams is a separate paid product. |
| **abliteration.ai** (`abliteration-ai`) | key/env | 3 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **above.dev** (`above`) | key/env | 10 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **AgentRouter** (`agentrouter`) | key/env | 5 | 5 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Agnes AI** (`agnes`) | key/env | 4 | 3 free | listed | 3 of 4 catalog models at $0 (agnes-3.0-flash, agnes-2.5-flash, agnes-2.0-flash). |
| **ai&** (`aiand`) | key/env | 10 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **AI-ROUTER** (`ai-router`) | key/env | 5 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **AI/ML API** (`aimlapi`) | key/env | 171 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **AI21 Labs** (`ai21`) | key/env | 2 | — | partial | Trial API keys with credit have been offered. |
| **AIHubMix** (`aihubmix`) | key/env | 154 | 16 free | listed | 16 $0 entries, mostly coding-*-free (coding-glm-5.3-free, coding-glm-5.2-free, glm-4.7-flash-free ...). |
| **ainetcafe** (`ainetcafe`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Aixy** (`aixy`) | key/env | 13 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **AKI.IO** (`aki-io`) | key/env | 7 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Alibaba** (`alibaba`) | key/env | 53 | 1 free | yes | Activate Model Studio in the Singapore region: every model gets its own free quota (typically 1,000,000 tokens) valid 90 days. |
| **Alibaba (China)** (`alibaba-cn`) | key/env | 80 | 3 free | yes | Bailian (百炼) new-user free quota per model (1M tokens typical) after real-name verification. |
| **Alibaba Coding Plan** (`alibaba-coding-plan`) | key/env | 10 | 10 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Alibaba Coding Plan (China)** (`alibaba-coding-plan-cn`) | key/env | 10 | 10 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Alibaba Token Plan** (`alibaba-token-plan`) | key/env | 29 | 29 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Alibaba Token Plan (China)** (`alibaba-token-plan-cn`) | key/env | 29 | 29 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Amazon Bedrock** (`amazon-bedrock`) | key/env + cloud creds | 200 | — | no | Paid via AWS; free trial credits for some models occasionally. |
| **Ambient** (`ambient`) | key/env | 10 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **AMD** (`amd`) | key/env | 11 | 11 free | partial | AMD Radeon Developer Cloud gives free API keys during beta (11 $0 models). |
| **Anthropic** (`anthropic`) | key/env | 17 | — | no | Paid API; Anthropic gives no free API tier |
| **AnyAPI** (`anyapi`) | key/env | 30 | 30 free | claimed | Homepage: free tier / "no credit card" / "Try for free". |
| **Arcee** (`arcee`) | key/env | 11 | — | partial | Free access to its own small models has been offered. |
| **Atomic Chat** (`atomic-chat`) | key/env | 5 | 5 free | local | Local app endpoint - free on your own hardware. |
| **Auriko** (`auriko`) | key/env | 15 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Azure** (`azure`) | key/env | 95 | 1 free | no | Paid; Azure free trial credits can be used |
| **Bailing** (`bailing`) | key/env | 2 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Baseten** (`baseten`) | key/env | 14 | — | partial | $30 trial credit. |
| **Bee by HEOSSI** (`bee`) | key/env | 6 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Berget.AI** (`berget`) | key/env | 6 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Blue Claw** (`blueclaw`) | key/env | 1 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Bothub** (`bothub`) | key/env | 8 | 2 free | partial | Some $0 routes (nemotron-3-ultra-550b-a55b:free, gemma-4-31b-it:free). |
| **Boundless** (`boundless`) | key/env | 20 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Cerebras** (`cerebras`) | key/env | 2 | — | partial | Free tier with daily token caps on a few fast models. |
| **Charm Hyper** (`hyper`) | key/env | 23 | — | partial | Formerly a free Hypercredit allowance per month (generous, no card); now retired - PAYG from $5, ZDR, no rate limits |
| **Chutes** (`chutes`) | key/env | 17 | 7 free | partial | Decentralised compute with a rotating free-ish set; 7 catalog entries at $0 (DeepSeek V4.1/V4 Pro, Qwen3.8, GLM-5.2). |
| **Clarifai** (`clarifai`) | key/env | 12 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Claudinio** (`claudinio`) | key/env | 2 | — | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **ClinePass** (`cline-pass`) | key/env | 18 | — | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **CloudFerro Sherlock** (`cloudferro-sherlock`) | key/env | 5 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Cloudflare AI Gateway** (`cloudflare-ai-gateway`) | key/env | 73 | 1 free | partial | Gateway has a free tier; model usage billed by the provider behind it. |
| **Cloudflare Workers AI** (`cloudflare-workers-ai`) | key/env | 28 | — | yes | Workers AI free tier: 10,000 Neurons/day with any Cloudflare account. |
| **Cohere** (`cohere`) | key/env | 17 | 7 free | partial | Free "trial" key with rate limits for evaluation; 7 $0 entries are Aya / North Mini Code 1.0 (promo). |
| **CommandCode** (`commandcode`) | key/env | 71 | 1 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Constellation Gate** (`gate`) | key | 0 | 2 free | partial | Marketing: "Free tier included - no credit card required" |
| **CoralBricks** (`coralbricks`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **CoreWeave** (`wandb`) | key/env | 23 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Cortecs** (`cortecs`) | key/env | 107 | 2 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **CrossModel** (`crossmodel`) | key/env | 68 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Crusoe** (`crusoe`) | key/env | 11 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **D.Run (China)** (`drun`) | key/env | 3 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **DaoXE** (`daoxe`) | key/env | 9 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Databricks** (`databricks`) | key/env | 31 | — | partial | Free trial / community edition credits. |
| **Deep Infra** (`deepinfra`) | key/env | 77 | — | partial | Small signup credits have been offered. |
| **DeepSeek** (`deepseek`) | key/env | 4 | — | no | No free tier |
| **DevPass (LLM Gateway)** (`llmgateway`) | key/env | 207 | 4 free | claimed | Homepage: free tier / no credit card; open-source gateway is also self-hostable for free. |
| **DigitalOcean** (`digitalocean`) | key/env + OAuth | 83 | 7 free | no | PAYG; 7 $0 entries are image/video models. |
| **DInference** (`dinference`) | key/env | 6 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **EBCloud** (`ebcloud`) | key/env | 4 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Echo** (`echo`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Eden AI** (`edenai`) | key/env | 369 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **EmpirioLabs AI** (`empiriolabs`) | key/env | 63 | 4 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **engy** (`engy`) | key/env | 9 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **evroc** (`evroc`) | key/env | 16 | 2 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Exa** (`exa`) | key/env | 0 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **FastRouter** (`fastrouter`) | key/env | 39 | 8 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Firecrawl** (`firecrawl`) | key/env | 0 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Fireworks AI** (`fireworks-ai`) | key/env | 29 | — | partial | $1 signup credit. |
| **FreeModel** (`freemodel`) | key/env | 10 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Friendli** (`friendli`) | key/env | 5 | — | partial | Signup credits have been offered. |
| **FrogBot** (`frogbot`) | key/env | 26 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **GitHub Copilot** (`github-copilot`) | env + OAuth | 35 | — | partial | Copilot Free (limited monthly completions/chat) works with OpenCode's device OAuth. |
| **GitLab Duo** (`gitlab`) | key/env + OAuth | 31 | 31 free | partial | Duo is seat-based; GitLab.com Free tier has limited Duo features. |
| **GMI Cloud** (`gmicloud`) | key/env | 17 | — | partial | Signup credits offered periodically. |
| **Google** (`google`) | key/env | 38 | 4 free | yes | AI Studio free tier key from https://aistudio.google.com/apikey |
| **GreenPT** (`greenpt`) | key/env | 40 | 2 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Groq** (`groq`) | key/env | 14 | 5 free | yes | Free developer tier with rate limits on open models (GPT-OSS, Llama, Whisper). |
| **Helicone** (`helicone`) | key/env | 90 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Hetzner** (`hetzner`) | key/env | 2 | 2 free | no | PAYG; 2 $0 entries are beta models. |
| **HPC-AI** (`hpc-ai`) | key/env | 9 | — | partial | Free trial credits per account. |
| **Hugging Face** (`huggingface`) | key/env | 81 | 1 free | partial | PAYG with no markup |
| **Impossibl** (`impossibl`) | key/env | 76 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Inception** (`inception`) | key/env | 4 | — | partial | Trial credits historically available. |
| **Inceptron** (`inceptron`) | key/env | 6 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Inco** (`inco`) | key/env | 7 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Infer by Flow7** (`infer`) | key/env | 2 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Inference** (`inference`) | key/env | 9 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **InferX** (`inferx`) | key/env | 12 | 12 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Infomaniak** (`infomaniak`) | key/env | 10 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **IO.NET** (`io-net`) | key/env | 17 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **IteraCompute** (`iteracompute`) | key/env | 10 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Jalapeno Cloud** (`jalapeno`) | key/env | 17 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Jiekou.AI** (`jiekou`) | key/env | 61 | — | listed | Homepage mentions free credits (免费); Chinese aggregator. |
| **Kenari** (`kenari`) | key/env | 64 | 24 free | listed | 24 $0 catalog entries. |
| **Kilo Gateway** (`kilo`) | key/env | 396 | 22 free | yes | "Start with Kilo Auto Free - No credit card required" plus 22 $0 catalog entries (kilo-auto/free, cohere/north-mini-code:free, reflection/beam-free... |
| **Kimi For Coding (kimi.ai)** (`kimi-code-plan-global`) | key/env | 6 | 6 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Kimi For Coding (kimi.com)** (`kimi-code-plan-cn`) | key/env | 6 | 6 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **klokintegration.se** (`klokintegration`) | key/env | 3 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Kosmik Compute** (`kosmik`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **KUAE Cloud Coding Plan** (`kuae-cloud-coding-plan`) | key/env | 1 | 1 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Lilac** (`lilac`) | key/env | 4 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Liquid Inference** (`liquid`) | key/env | 1 | 1 free | no | Own model listed at $0 on its router. |
| **LLM Gateway** (`llmgateway-providers`) | key/env | 430 | 2 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **LLM Tech** (`llmtech`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **LLMTR** (`llmtr`) | key/env | 32 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **LMStudio** (`lmstudio`) | key/env | 3 | 3 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **LongCat** (`longcat`) | key/env | 2 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **LowRouter** (`lowrouter`) | key/env | 31 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **LucidQuery** (`lucidquery`) | key/env | 4 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Lynkr** (`lynkr`) | key/env | 1 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Meganova** (`meganova`) | key/env | 19 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Melious** (`melious`) | key/env | 13 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Merge Gateway** (`merge-gateway`) | key/env | 201 | 2 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Meta** (`meta`) | key/env | 6 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **MiniMax (minimax.cn)** (`minimax-cn`) | key/env | 8 | — | no | Same as minimax.io, China billing region. |
| **MiniMax (minimax.io)** (`minimax`) | key/env | 8 | — | no | No standing free tier - pay-as-you-go; MiniMax-M3 has a permanent 50% discount. |
| **MiniMax Token Plan (minimax.cn)** (`minimax-cn-coding-plan`) | key/env | 9 | 9 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **MiniMax Token Plan (minimax.io)** (`minimax-coding-plan`) | key/env | 9 | 9 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Mistral** (`mistral`) | key/env | 34 | 4 free | partial | Free chat/Vibe plan costs $0 but gives no API key; La Plateforme's free "Experiment" tier has been rate-limited |
| **Mixlayer** (`mixlayer`) | key/env | 5 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Moark** (`moark`) | key/env | 10 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Modal** (`modal`) | key/env | 8 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Model Oracle AI** (`model-oracle-ai`) | key/env | 15 | 15 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Modelis** (`modelis`) | key/env | 9 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **ModelScope** (`modelscope`) | key/env | 7 | 7 free | yes | ModelScope (Alibaba) free API after binding an Alibaba Cloud account; generous daily call quota. |
| **Moonshot AI** (`moonshotai`) | key/env | 6 | — | no | Trial credits have been given in some regions. |
| **Moonshot AI (China)** (`moonshotai-cn`) | key/env | 6 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Morph** (`morph`) | key/env | 11 | — | no | Paid apply-code models. |
| **Munito AI** (`munito`) | key/env | 5 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Munito AI (EU)** (`munito-eu`) | key/env | 4 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **NaN** (`nan`) | key/env | 8 | 8 free | listed | 8 $0 entries (deepseek-v4-flash, glm5.3-flash, qwen3.6, gemma4, mimo-v2.6-flash). |
| **NanoGPT** (`nano-gpt`) | key/env | 649 | 4 free | partial | No free tier or subscription credits: PAYG only |
| **NEAR AI Cloud** (`nearai`) | key/env | 56 | 1 free | no | Confidential PAYG inference; 1 $0 entry is an image model. |
| **Nebius Token Factory** (`nebius`) | key/env | 26 | — | partial | Trial credit for new accounts. |
| **Neon** (`neon`) | key/env | 57 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **NeoSmith** (`neosmith`) | key/env | 4 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Neuralwatt** (`neuralwatt`) | key/env | 23 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Nova** (`nova`) | key/env | 2 | 2 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Novita AI** (`novita-ai`) | key/env | 89 | 1 free | partial | Signup credits plus periodic free-model promos. |
| **Nvidia** (`nvidia`) | key/env | 52 | 23 free | yes | NVIDIA Build trial API: sign up at build.nvidia.com and use the trial endpoints |
| **OCI Generative AI** (`oci`) | key/env | 9 | — | partial | Oracle Cloud Free Tier credits can be used. |
| **Ofox** (`ofox`) | key/env | 148 | — | claimed | Homepage: "free tier", "no credit card". |
| **ollama** (`ollama`) | key | 0 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Ollama Cloud** (`ollama-cloud`) | key/env | 23 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **OpenAI** (`openai`) | key/env + OAuth + OAuth + OAuth | 51 | 4 free | partial | API is paid, but OpenCode can sign in with a ChatGPT Plus/Pro plan via OAuth (usage counts against your plan), and codex/ChatGPT plans are cheaper ... |
| **OpenCode Console** (`opencode`) | key/env + OAuth | 130 | 9 free | yes | Free models need no key at all, or sign in with an OpenCode Console account |
| **OpenCode Go** (`opencode-go`) | key/env | 37 | 6 free | partial | $10/$40 mo subscription that includes usage; "Beam Free" is $0 and unlimited on it. |
| **OpenReason** (`openreason`) | key/env | 3 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **OpenRouter** (`openrouter`) | key/env | 389 | 21 free | yes | Create a key and call models whose ID ends in :free (24 in models.dev; 21 enabled here). |
| **Opper** (`opper`) | key/env | 55 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **OrcaRouter** (`orcarouter`) | key/env | 117 | 8 free | partial | Homepage: free credits, no credit card; 8 $0 entries (glm-5.3-flash-free, deepseek-v4-flash-free, orcarouter/auto ...). |
| **OVHcloud AI Endpoints** (`ovhcloud`) | key/env | 12 | 2 free | no | PAYG; 2 $0 entries are Qwen3Guard safety models. |
| **Parallel** (`parallel`) | key/env | 0 | — | claimed | Homepage advertises a "free plan" (web research API, not LLM chat). |
| **Pareto Inference** (`pareto`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Pendra** (`pendra`) | key/env | 6 | 6 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Perplexity** (`perplexity`) | key/env | 4 | — | no | Paid; Pro subscribers get $5/month of API credits. |
| **Perplexity Agent** (`perplexity-agent`) | key/env | 45 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Pioneer** (`pioneer`) | key/env | 25 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Poe** (`poe`) | key/env + OAuth | 139 | 44 free | partial | Free plan gives daily points on poe.com; API access is for subscribers (44 $0 entries are media bots). |
| **Poolside** (`poolside`) | key/env | 3 | 3 free | no | Paid; 3 $0 entries are beta-priced. |
| **Prime Inference** (`prime`) | key/env | 70 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Privatemode AI** (`privatemode-ai`) | key/env | 11 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **QiHang** (`qihang-ai`) | key/env | 9 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Qiniu** (`qiniu-ai`) | key/env | 87 | 37 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **QVAC** (`qvac`) | key/env | 9 | 9 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Reflection** (`reflection`) | key/env | 1 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Regolo AI** (`regolo-ai`) | key/env | 18 | 3 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Requesty** (`requesty`) | key/env | 183 | 12 free | partial | Requesty advertises a free tier / credits on its site; 12 $0 catalog routes. |
| **routing.run** (`routing-run`) | key/env | 15 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **RunInfra** (`runinfra`) | key/env | 8 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Sakana AI** (`sakana`) | key/env | 4 | 1 free | no | Paid; 1 $0 entry is a promo. |
| **SaladCloud AI Gateway** (`salad-cloud`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **SambaNova** (`sambanova`) | key/env | 6 | — | partial | Free developer tier historically available. |
| **SAP AI Core** (`sap-ai-core`) | key/env | 51 | 12 free | partial | SAP BTP trial gives AI Core credits. |
| **Sarvam AI** (`sarvam`) | key/env | 2 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Scaleway** (`scaleway`) | key/env | 17 | 1 free | no | PAYG; 1 $0 entry is Whisper. |
| **SCNet Token Plan** (`scnet-token-plan`) | key/env | 19 | 19 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **SCX.ai** (`scx-ai`) | key/env | 4 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **SenseNova (China)** (`sensenova`) | key/env | 6 | 6 free | no | All 6 catalog models listed at $0 - believed to be a signup credit, not a standing tier. |
| **SiliconFlow** (`siliconflow`) | key/env | 57 | — | partial | New international accounts get $1 in free credits; cheapest models are $0.04/M. |
| **SiliconFlow (China)** (`siliconflow-cn`) | key/env | 40 | 5 free | listed | Chinese platform has historically offered free models (Qwen/Qwen3-8B, DeepSeek-OCR, Qwen3.5-4B, Qwen2.5-7B) marked 免费 plus signup giveaways. |
| **Snowflake Cortex** (`snowflake-cortex`) | key/env + OAuth | 25 | 3 free | partial | Trial accounts include Snowflake credits. |
| **STACKIT** (`stackit`) | key/env | 8 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Standard Compute** (`standardcompute`) | key/env | 40 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **StepFun (China)** (`stepfun`) | key/env | 7 | 3 free | no | Paid; 3 $0 entries are TTS/ASR beta. |
| **StepFun (Global)** (`stepfun-ai`) | key/env | 7 | 3 free | no | Paid; 3 $0 entries are TTS/ASR beta. |
| **StepFun Step Plan (China)** (`stepfun-step-plan`) | key/env | 5 | 5 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **StepFun Step Plan (Global)** (`stepfun-ai-step-plan`) | key/env | 4 | 4 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Subconscious** (`subconscious`) | key/env | 2 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **submodel** (`submodel`) | key/env | 9 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Synthetic** (`synthetic`) | key/env | 12 | — | no | Paid subscription for open models. |
| **Tavily** (`tavily`) | key/env | 0 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Tempr Gateway** (`tempr`) | key/env | 82 | 6 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Tencent Coding Plan (China)** (`tencent-coding-plan`) | key/env | 8 | 8 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Tencent Token Plan** (`tencent-token-plan`) | key/env | 2 | 1 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Tencent TokenHub** (`tencent-tokenhub`) | key/env | 3 | 2 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **TensorX** (`tensorx`) | key/env | 25 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **The Grid AI** (`the-grid-ai`) | key/env | 17 | 17 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Thinking Machines** (`thinkingmachines`) | key/env | 38 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Tinfoil** (`tinfoil`) | key/env | 8 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **TinyFish** (`tinyfish`) | key/env | 0 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Together AI** (`togetherai`) | key/env | 32 | — | partial | Signup credit ($1-$5 historically). |
| **TokenGo** (`tokengo`) | key/env | 13 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **TokenRouter** (`tokenrouter`) | key/env | 1 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **TrustedRouter** (`trustedrouter`) | key/env | 7 | 7 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Umans AI** (`umans-ai`) | key/env | 8 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Umans AI Coding Plan** (`umans-ai-coding-plan`) | key/env | 9 | 9 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **UnoRouter** (`unorouter`) | key/env | 23 | 11 free | yes | Sign up, use any model whose ID ends in :free (minimax-m3.1-flash:free, deepseek-v4.1-flash-1017:free, step-5-preview:free, mimo-v2.6-flash:free, n... |
| **Upstage** (`upstage`) | key/env | 5 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Vancine** (`vancine`) | key/env | 8 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Venice AI** (`venice`) | key/env | 128 | — | partial | Homepage advertises a free tier / no credit card. |
| **Vercel AI Gateway** (`vercel`) | key/env | 416 | 134 free | no | PAYG; some Vercel plans include monthly AI credits |
| **Vertex** (`google-vertex`) | key/env + cloud creds | 61 | — | no | Paid via GCP |
| **Vispark** (`vispark`) | key/env | 3 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Vivgrid** (`vivgrid`) | key/env | 37 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Volcengine Ark** (`volcengine`) | key/env | 16 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Volcengine Ark Coding Plan** (`volcengine-coding-plan`) | key/env | 10 | 10 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Vultr** (`vultr`) | key/env | 15 | — | partial | $250 / 30-day promo credits for new accounts. |
| **Wafer** (`wafer.ai`) | key/env | 5 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Wallaby** (`wallaby`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **watsonx.ai** (`watsonx`) | key/env | 5 | — | partial | IBM Cloud Lite plan has included inference units. |
| **xAI** (`xai`) | key/env + OAuth | 13 | 5 free | no | Paid; 5 $0 entries are Grok Imagine media. |
| **Xiaomi** (`xiaomi`) | key/env | 6 | — | partial | New-account welcome bonus credits; Token Plan subscriptions from $6/mo (include free TTS) |
| **Xiaomi Token Plan (China)** (`xiaomi-token-plan-cn`) | key/env | 7 | 7 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Xiaomi Token Plan (Europe)** (`xiaomi-token-plan-ams`) | key/env | 7 | 7 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Xiaomi Token Plan (Singapore)** (`xiaomi-token-plan-sgp`) | key/env | 7 | 7 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Xpersona** (`xpersona`) | key/env | 13 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Z.AI** (`zai`) | key/env | 18 | 3 free | partial | 3 GLM models are free: glm-4.5-flash, glm-4.7-flash, glm-4.6v-flash. |
| **Z.AI Coding Plan** (`zai-coding-plan`) | key/env | 7 | 7 free | no | Subscription plan with monthly/weekly quotas - not a free tier |
| **Zeldoc** (`zeldoc`) | key/env | 1 | 1 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Zenifra** (`zenifra`) | key/env | 1 | — | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **ZenMux** (`zenmux`) | key/env | 110 | 6 free | not checked | No public free tier found on the provider's homepage and no $0 chat models in models.dev |
| **Zhipu AI** (`zhipuai`) | key/env | 17 | 3 free | partial | Same GLM free flash models on the China endpoint. |
| **Zhipu AI Coding Plan** (`zhipuai-coding-plan`) | key/env | 4 | 4 free | no | Subscription plan with monthly/weekly quotas - not a free tier |

</details>

---

## Free-tier cheat sheet per family

| Family | Providers | Free angle |
| :-- | :-- | :-- |
| OpenCode's own | `opencode`, `opencode-go` | 9 free models no-key; Go subscription has Beam Free |
| Frontier labs / clouds | `openai`, `anthropic`, `google`, `google-vertex`, `azure`, `amazon-bedrock`, `xai`, `meta`, `mistral`, `cohere`, `perplexity` | Google Flash free tier, Copilot/OpenAI OAuth via ChatGPT plan, cloud trial credits only |
| Aggregators / gateways | `openrouter`, `unorouter`, `kilo`, `anyapi`, `llmgateway`, `vercel`, `poe`, `requesty`, `orcarouter`, `nano-gpt`, `chutes`, `ofox`, `llmgateway-providers`, `merge-gateway`, `helicone`, `zenmux`, `tempr`, `fastrouter`, `lowrouter`, `trustedrouter`, `tokenrouter`, `cmd` | `:free` suffixes, free auto-model tiers, small credits |
| GPU clouds / inference hosts | `nvidia`, `cloudflare-workers-ai`, `baseten`, `fireworks-ai`, `together`, `deepinfra`, `nebius`, `sambanova`, `groq`, `cerebras`, `novita-ai`, `scaleway`, `ovhcloud`, `hetzner`, `vultr`, `gmicloud`, `hpc-ai`, `friendli`, `inception`, `arcee` | NVIDIA/Cloudflare/Groq/Cerebras free tiers, otherwise signup credits |
| Chinese platforms | `alibaba`, `alibaba-cn`, `modelscope`, `siliconflow-cn`, `qiniu-ai`, `zai`, `zhipuai`, `sensenova`, `stepfun`, `stepfun-ai`, `moonshotai`, `minimax-cn`, `volcengine`, `tencent-*`, `longcat`, `bailing`, `jiekou`, `d.run` | New-user free quotas, free GLM Flash, free Qwen on ModelScope |
| Subscription plans (never free) | `opencode-go`, `minimax-coding-plan`, `minimax-cn-coding-plan`, `kimi-code-plan-*`, `zai-coding-plan`, `zhipuai-coding-plan`, `alibaba-coding-plan*`, `alibaba-token-plan*`, `stepfun*-step-plan`, `xiaomi-token-plan-*`, `tencent-coding-plan`, `tencent-token-plan`, `tencent-tokenhub`, `volcengine-coding-plan`, `scnet-token-plan`, `kuae-cloud-coding-plan`, `umans-ai-coding-plan`, `cline-pass`, `claudinio`, `commandcode` | Paid plans with monthly quotas |
| Local | `ollama`, `lmstudio`, `atomic-chat`, `lynkr`, `privatemode-ai`, `qvac` (local runtime) | Free on your hardware |
| Enterprise clouds | `snowflake-cortex`, `databricks`, `sap-ai-core`, `watsonx`, `oci`, `gitlab`, `azure`, `amazon-bedrock`, `google-vertex`, `cloudflare-ai-gateway` | Trial credits from the parent cloud account |
| Tools (not LLMs) | `exa`, `tavily`, `firecrawl`, `parallel`, `tinyfish`, `morph` | Separate search/scrape free tiers on their own sites |

---

## Reproduce

```bash
# 1. Start a private OpenCode server (prints a password)
opencode serve --hostname 127.0.0.1 --port 4097

# 2. Provider catalog + enabled models
PW=<password from step 1>
curl -s -u "opencode:$PW" http://127.0.0.1:4097/api/integration -o data/integration.json
curl -s -u "opencode:$PW" http://127.0.0.1:4097/api/model       -o data/model.json

# 3. The upstream catalog OpenCode builds on
curl -s https://models.dev/api.json -o data/models.dev.json

# 4. CLI view of what is enabled right now
opencode models | cut -d/ -f1 | sort | uniq -c | sort -rn
```

```bash
# Zero-cost models currently enabled, per provider
python3 - <<'EOF'
import json
d = json.load(open('data/model.json'))['data']
free = [m for m in d if not (m['cost'][0].get('input') or 0) and not (m['cost'][0].get('output') or 0)]
for m in sorted(free, key=lambda m: (m['providerID'], m['id'])):
    print(m['providerID'] + '/' + m['id'])
EOF
```

```bash
# Free tiers change: compare your catalog with models.dev
curl -s https://models.dev/api.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(len(d), 'providers in catalog')"
```

---

## Freshness and caveats

- **Everything here expires.** Vendors rotate `:free` models weekly (OpenRouter, UnoRouter, Kilo), OpenCode's free lineup is explicitly "limited time", and Alibaba's free quota changed rules on 2026-09-08 and again in Oct 2026.
- **`$0` in a catalog is not the same as free to use.** models.dev lists `$0` for beta models, media models that bill per image, TTS/ASR endpoints, promo models and safety models. `data/providers.csv` keeps the raw `$0` counts separate from the verified `free` verdict so you can see the difference.
- **Free tiers are usually for evaluation.** Expect lower rate limits (RPM/TPM/RPD), data being used for training on some free tiers (Google free tier, NVIDIA trial, many `:free` routes), and no SLA.
- **Region matters.** Alibaba free quotas, SiliconFlow CN, Xiaomi Token Plan regions, Beam Free's blocklist, and OpenAI/Gemini available regions all differ.
- **`gate`** (Constellation Gate) is a custom provider configured manually in OpenCode's config (not part of models.dev); its "free tier" is a marketing claim.
- **Auth is not the same as free.** Several providers (Copilot, OpenAI via ChatGPT plan, GitLab Duo, Poe) can be used without a *paid API bill* because a subscription you already have covers them.

## Contributing

Open an issue/PR with the provider ID and a link to the vendor's pricing page if a row is stale. Keep the `evidence_status` honest: `verified` needs a vendor URL, `claimed` means marketing only, `not checked` means no free offer found.
