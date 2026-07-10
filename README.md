# Composio SaaS API Research Pipeline & Agent Readiness Audit

This repository contains the source code, raw data inputs, and the final interactive executive dashboard for evaluating **100 SaaS applications** across 10 categories to determine their API buildability and AI agent readiness.

---

## 1. Project Folder Structure

```
├── application_catalog.json   # Synced database of 100 SaaS apps to evaluate
├── data_models.py             # Shared Python dataclasses 
├── research_worker.py         # Scraping worker with fallback heuristics
├── pipeline.py                # Pipeline Orchestrator running fetches & audits
├── generate_dashboard.py      # Combines results into a self-contained web page
├── index.html                 # Final interactive dark-theme case study dashboard
├── requirements.txt           # Clean requirements (aiohttp, beautifulsoup4, requests)
└── results/
    ├── results.json           # Raw JSON dataset output database
    ├── results.csv            # Structured tabular CSV export
    └── verification_report.md # Measured accuracy stats & human review logs
```

---

## 2. System Architecture & Workflows

### System Topology Diagram
```
[application_catalog.json]
       │
       ▼
[pipeline.py (Orchestrator)] ──► [research_worker.py (Fetcher & Matcher)] ──► [DuckDuckGo Fallback Search]
       │
       ▼
[results/results.json] ──► [results/results.csv]
       │
       ▼
[index.html (Single-page Executive Case Study Dashboard - Tailwind & Chart.js)]
```

### Research Agent & Fetcher Workflow
1. **Direct Request Pass**: Fetches the API documentation URL with custom headers to simulate a normal browser request.
2. **Search fallback**: If blocked (403 Cloudflare, redirects), triggers DuckDuckGo query scraper fallbacks targeting developer authorization setup docs.
3. **Regex Heuristics Engine**: Evaluates auth type, self-serve developer signup support, REST/GraphQL support, webhooks presence, and pre-existing MCP servers.
4. **Explainable Buildability Score Calculation**: Dynamically computes integration value from 0 to 100 and flags human validation requirements.

---

## 3. Installation & Local Setup

### Prerequisites
Ensure you have Python 3.8+ installed.

### Setup Steps
1. **Clone & Navigate**:
   ```bash
   cd "assignment of ai product intern"
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Execute the Research Pipeline**:
   ```bash
   python pipeline.py
   ```
4. **Generate the Web Case Study Dashboard**:
   ```bash
   python generate_dashboard.py
   ```

---

## 4. Key Metrics & Output Sample
The results are compiled in the `results/` folder:
- **`results.json`**: Full structured document containing description, auth types, REST/GraphQL, webhooks, and raw source links.
- **`verification_report.md`**: Tracks measured accuracy:
  - **Direct Scraper Fetch Success Rate**: 84.0%
  - **Initial Automated Accuracy**: 80.0%
  - **Post-Verification Accuracy**: 100.0% (Resolved via Fallbacks)
  - **Accuracy Gain**: +20.0%

---

## 5. Reviewer Verification Guide
To review the interactive case study dashboard:
1. Open the file **`index.html`** in any web browser (Chrome, Safari, Edge, Firefox).
2. Because the dataset is embedded directly in the HTML code, you will **not experience local CORS blocking issues** (allowing direct review under `file:///` protocols without running a local node server).
3. Search, sort, and select filters (e.g. show *High Buildability* or *OAuth2* only). Click on any application row to slide open the **Evidence Trace Drawer** displaying verified developer links and blockers.
