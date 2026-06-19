# 100Hires Portfolio Project

## Overview

This repository documents the completion of the 100Hires portfolio project. The project involves researching expert voices in **AI-Powered SEO Content Production** and collecting their content to build a playbook for using AI to produce, scale, and optimize SEO content for B2B SaaS companies.

---

## Step 1: Environment Setup

### Tools Installed

* **Cursor IDE** — Primary development environment
* **Claude Code Extension** — Installed via Cursor Extensions Marketplace
* **Codex Extension** — Installed and authenticated
* **Git** — Version control
* **GitHub** — Public repository hosting
* **Antigravity** — AI-assisted development

### Steps Completed

1. Installed Cursor IDE
2. Installed the Claude Code extension
3. Installed the Codex extension
4. Created a public GitHub repository
5. Documented the setup process

---

## Step 2: Expert Research & Content Collection

### Topic: AI-Powered SEO Content Production

**Research Goal:** Build a playbook for using AI to produce, scale, and optimize SEO content for B2B SaaS companies.

### Why These Experts?

These 10 experts were selected because they **practice what they teach** — they run agencies, build tools, lead SEO at real companies, and publish primary research. They are not just writers or commentators; they're practitioners with documented workflows and measurable results.

| Expert | Role | Why They're Credible |
|--------|------|---------------------|
| **Kevin Indig** | Growth Advisor (ex-Shopify, Atlassian, Reddit) | Ran SEO at massive product-led SaaS companies. Publishes weekly data-driven experiments in Growth Memo newsletter. |
| **Lily Ray** | VP SEO & AI Search, Amsive + Founder, Algorythmic | The industry's go-to analyst for Google quality guidelines and AI content strategy. |
| **Aleyda Solis** | Founder, Orainti | Built free public curricula (LearningSEO.io, LearningAIsearch.com). Documents how AI crawlers differ from Googlebot. |
| **Ross Hudgens** | Founder & CEO, Siege Media (Inc. 5000) | Analyzed 12,000 URLs across B2B/B2C. Writing a Wiley book on GEO (Q4 2026). |
| **Brendan Hufford** | Founder, Growth Sprints (ex-ActiveCampaign) | Publicly documented high-output SEO content programs for SaaS with small teams. |
| **Kyle Roof** | Lead SEO, High Voltage SEO; Inventor, PageOptimizer Pro | Holds US patent for SEO testing methodology. 400+ peer-reviewed SEO tests. |
| **Bernard Huang** | Founder & CEO, Clearscope | Runs the content optimization tool used by HubSpot, Adobe, Condé Nast. |
| **Eli Schwartz** | Product-Led SEO consultant (ex-SurveyMonkey) | Wrote *Product-Led SEO* — the most cited book in this space. |
| **Nathan Gotch** | Founder, Rankability; Gotch SEO Academy | One of the most active practitioners documenting step-by-step AI SEO workflows. |
| **Steve Toth** | CEO, Notebook Agency; ex-SEO Lead, FreshBooks | SEO Notebook newsletter is one of the most subscribed practitioner-focused SEO emails. |

### What Was Collected

#### YouTube Transcripts (14 videos, 118,000+ words)
Fetched using the **`youtube-transcript-api`** Python library — free, open-source, no API key required.

| Expert | Video | Words |
|--------|-------|-------|
| Nathan Gotch | *Is SEO finally dead — New 2026 study* | 5,630 |
| Nathan Gotch | *7-Step SEO Campaign Checklist for 2026* | 2,497 |
| Aleyda Solis | *Learn SEO with a Roadmap (LearningSEO.io)* | 355 |
| Aleyda Solis | *Join the LRT SEOKtoberfest Challenge* | 238 |
| Bernard Huang | *The Future of Search (panel: Lily Ray, Kevin Indig, Ross Hudgens, Steve Toth)* | 12,965 |
| Bernard Huang | *AI SEO After the Hype — What Actually Works in 2026* | 11,200 |
| Kyle Roof | *Best LLM for SEO 2026 (GPT-5.2, Claude 4.6, Grok 4.2 tested)* | 1,433 |
| Kyle Roof | *Which LLM is Best for SEO* | 11,574 |
| Kevin Indig | *SEO in the Age of AI — Google Overviews & Future of Search* | 11,247 |
| Eli Schwartz | *Product-Led SEO in AI Era* | 10,965 |
| Eli Schwartz | *Stop Chasing AI Citations — SEO, Google AI Mode* | 16,425 |
| Ross Hudgens | *What Your CMO Needs to Know About AI Search* | 14,717 |
| Brendan Hufford | *SEO Mistakes to Avoid* | 7,459 |
| Lily Ray | *20 for 20 — Navigating AI Search Overviews* | 11,781 |

#### LinkedIn Posts (Templates for Manual Collection)
LinkedIn has no public API for retrieving posts. Templates with instructions are provided for manually collecting 2-3 recent posts per expert.

#### Other Materials
- **Newsletters overview** — Descriptions and links for 4 expert newsletters (Growth Memo, SEOFOMO, Product-Led SEO, SEO Notebook)
- **Tools & Resources** — Catalog of tools built by these experts (Clearscope, Rankability, PageOptimizer Pro, etc.) plus free learning resources and upcoming publications

### Repository Structure

```
100hires-step1/
├── readme.md                          # This file
├── research/
│   ├── sources.md                     # 10 experts with links, dates, annotations
│   ├── youtube-transcripts/           # 14 transcript files organized by expert
│   │   ├── nathan-gotch_*.md
│   │   ├── aleyda-solis_*.md
│   │   ├── bernard-huang_*.md
│   │   ├── kyle-roof_*.md
│   │   ├── kevin-indig_*.md
│   │   ├── eli-schwartz_*.md
│   │   ├── ross-hudgens_*.md
│   │   ├── brendan-hufford_*.md
│   │   ├── lily-ray_*.md
│   │   └── steve-toth_*.md
│   ├── linkedin-posts/                # Templates for manual post collection
│   │   ├── kevin-indig.md
│   │   ├── lily-ray.md
│   │   ├── aleyda-solis.md
│   │   ├── ross-hudgens.md
│   │   ├── brendan-hufford.md
│   │   ├── kyle-roof.md
│   │   ├── bernard-huang.md
│   │   ├── eli-schwartz.md
│   │   ├── nathan-gotch.md
│   │   └── steve-toth.md
│   └── other/
│       ├── newsletters.md             # Expert newsletter summaries
│       └── tools-and-resources.md     # Tools, consultancies, learning resources
└── scripts/
    └── fetch_transcripts.py           # YouTube transcript fetcher script
```

### Technical Methods Used

| Task | Tool / Method | Notes |
|------|---------------|-------|
| YouTube transcripts | `youtube-transcript-api` (Python) | Free, open-source, no API key. v1.2.4 with instance-based API. |
| LinkedIn posts | Manual collection (templates provided) | No free API exists. Scraping violates LinkedIn ToS. |
| Repository management | Git + GitHub | Incremental commits at each phase. |
| AI-assisted development | Antigravity IDE | Used for script creation, research, and content organization. |

---

## Challenges Encountered

### Claude Code Authentication (Step 1)
The Claude Code extension was installed but requires an active Claude subscription for authentication.

### YouTube Video ID Discovery (Step 2)
Initial video IDs from web search were not accurate. Solved by using browser automation to extract real video IDs directly from YouTube channel page DOMs. This yielded a 100% success rate (14/14 videos fetched).

### LinkedIn API Limitations (Step 2)
LinkedIn has no public API for retrieving user posts. All major methods (scraping, unofficial APIs) either violate LinkedIn ToS or require paid services. The practical solution is manual collection, which we provide templates for.

---

## Additional Context

I regularly use AI-assisted development tools as part of my workflow, including Antigravity, Factory AI, Zed, Cursor, Codex, and Kiro. These tools were used for code generation, research, content organization, and workflow automation throughout this project.
