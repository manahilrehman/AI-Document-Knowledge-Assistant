# AI Document Knowledge Assistant & Q&A App

> **A 4-Week AI Capstone Project** built using Python, LangChain, OpenAI APIs, Vector Database (FAISS/Chroma), and Streamlit.

---

## 📌 Project Overview
The **AI Document Knowledge Assistant & Q&A App** is an interactive, enterprise-ready Retrieval-Augmented Generation (RAG) system. It enables teams and users to upload internal documentation (PDFs, Markdown) and ask questions in natural language. The system retrieves the most relevant context and generates accurate, synthesized answers with verified source citations in **less than 2 seconds**.

### Target Benchmark Scenario: Acme Cloud Integration (SaaS Startup)
* **Problem:** 200+ internal product markdown docs and PDFs cause employees and trial users to waste hours searching for technical answers.
* **Solution:** An AI assistant that ingests company docs, performs semantic search, and delivers instant answers with exact source citations.

---

## 📂 Project Directory Structure

```text
AI-Document-Knowledge-Assistant/
├── docs/                                  # Strategic Project Documentation
│   ├── BASELINE_AUDIT_REPORT.md           # Week 1: Current workflow & tool audit
│   └── PROJECT_CHARTER_AND_KPIS.md        # Week 1: Goals, scope & KPI benchmarks
├── data/
│   └── sample_docs/                       # Sample documentation files (Markdown/PDF)
│       └── acme_cloud_overview.md         # Example SaaS knowledge base file
├── src/                                   # Source Code (Core Implementation)
│   ├── __init__.py
│   └── app.py                             # Streamlit UI & Application Entry Point
├── .env.example                           # Template for environment variables (API keys)
├── .gitignore                             # Files excluded from version control
├── requirements.txt                       # Python dependencies
└── README.md                              # Main project documentation & setup guide
```

---

## 🚀 Weekly Execution Milestones

| Milestone | Focus | Deliverables | Status |
| :--- | :--- | :--- | :--- |
| **Week 1** | **Scope Definition & Baseline Analysis** | Baseline Audit Report, Project Charter & KPIs, Workspace Setup | **✅ Completed** |
| **Week 2** | **Framework & Workflow Design** | Core Framework Draft, Standardized Templates, Test Scenario Log | **✅ Completed** |
| **Week 3** | **Execution & Tool Integration** | Integrated Tool Workflows, Pilot Execution Data, SLA Checklist | **✅ Completed** |
| **Week 4** | **Implementation, SOPs & Final Demo** | Final SOP Docs, Executive Deck, Portfolio Case Study, Video Guide | **✅ Completed** |

---

## 🛠️ Technology Stack
* **Language:** Python 3.10+
* **Framework:** LangChain
* **LLM & Embeddings:** OpenAI (`gpt-4o-mini`, `text-embedding-3-small`)
* **Vector Store:** FAISS / ChromaDB
* **Frontend:** Streamlit
* **Document Loaders:** PyPDF, Unstructured, LangChain Community Loaders

---

## ⚙️ Setup & Installation Instructions

### 1. Clone or Open the Repository
```bash
git clone <repository_url>
cd "AI Document Knowledge Assistant & Q&A App"
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Copy `.env.example` to a new file named `.env` and add your OpenAI API key:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Launch the Application
```bash
streamlit run src/app.py
```

---

## 🎯 Key Performance Indicators (KPIs)
* **Response Latency:** `< 2.0s` average query response time.
* **Citation Accuracy:** `≥ 90%` verifiable references with document name and section.
* **Hallucination Prevention:** `< 5%` false responses (strictly grounded in retrieved docs).

---

## 👤 Author
* **Project Role:** AI Ambassador & Engineering Intern
* **Program:** DataCrumbs Ambassador & Capstone Internship Program

