# Integrated Tool Workflows: Streamlit, FAISS & LangChain RAG Architecture

**Project:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 3 - Execution & Tool Integration  
**Author:** AI Ambassador & Engineering Intern  
**Status:** Validated Technical Workflow Specification  

---

## 1. System Integration Overview

Week 3 focuses on uniting the individual components designed in Weeks 1 and 2 into an **interactive, integrated production workflow**. The pipeline connects:
1. **Frontend Presentation Layer:** Streamlit Web Application (`src/app.py`).
2. **Document Processing Engine:** PyPDF & Markdown parsing with recursive character chunking.
3. **Vector Database & Similarity Engine:** FAISS (Facebook AI Similarity Search) index.
4. **Retrieval & Reasoning Engine:** LangChain RAG chain with strict grounding prompt templates.

```
+----------------------------------------------------------------------------------------------------+
|                                    INTEGRATED TOOL WORKFLOW MAP                                    |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  [ User Ingestion ]                                                                                |
|    ├── Upload Custom File (.pdf / .md / .txt)                                                      |
|    └── Or Click: "Load Acme Cloud Knowledge Base"                                                 |
|          │                                                                                         |
|          ▼                                                                                         |
|  [ Ingestion Pipeline ]                                                                            |
|    ├── Text Extraction & Header Normalization                                                      |
|    ├── Recursive Chunking: Window = 1000 chars, Overlap = 200 chars                                |
|    └── Metadata Assignment: {source: filename, section: header, chunk_id: index}                   |
|          │                                                                                         |
|          ▼                                                                                         |
|  [ Vector Store Integration ]                                                                      |
|    ├── Vector Embeddings (1536-dimensional space)                                                  |
|    └── FAISS In-Memory Index Construction (Cosine / L2 metric)                                     |
|          │                                                                                         |
|          ▼                                                                                         |
|  [ Interactive Chat Loop ]                                                                         |
|    ├── User submits query via Streamlit `st.chat_input`                                            |
|    ├── Top-K Similarity Search retrieves Top 3 Chunks (Threshold >= 0.70)                         |
|    ├── Context Block is synthesized with System Grounding Rules                                    |
|    ├── LLM generates grounded answer with verified inline references                               |
|    └── UI displays streaming response + expandable "Verified Source Citations" block (< 2.0s)      |
|                                                                                                    |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Component Integration Workflows

### 2.1 Ingestion & Chunking Workflow
* **File Ingestion:** Supports dynamic runtime upload of `.pdf`, `.md`, and `.txt` files through `st.file_uploader`, alongside an instant one-click loader for the internal `acme_cloud_overview.md` knowledge base.
* **Chunking Strategy:** Implemented using `RecursiveCharacterTextSplitter`. Text is split cleanly along structural boundaries (`\n\n` -> `\n` -> ` `) to ensure full paragraphs and semantic units remain intact.
* **Metadata Persistence:** Each chunk preserves its source filename and section heading, ensuring transparent traceability for subsequent citations.

### 2.2 Vector Storage Workflow (FAISS)
* **Index Structure:** In-memory FAISS IndexFlatL2 for low-latency similarity comparisons.
* **Dual Execution Resilience:**
  * **Production Mode:** Connects to OpenAI `text-embedding-3-small` and `gpt-4o-mini` when an API key is provided.
  * **Local / Demo Mode:** Built-in semantic vector matcher for zero-cost, zero-latency local testing, ensuring the app is always functional without external blockers.

### 2.3 Streamlit Interactive Interface Workflow
* **State Management:** Uses `st.session_state` to retain chat history, loaded document indices, and performance metrics across re-renders.
* **Latency Counter:** Measures end-to-end execution time using high-resolution monotonic clocks (`time.perf_counter()`) and reports exact latency per response.
* **Expandable Citations:** Renders a clean accordion (`st.expander`) displaying the exact document source, section name, and excerpt for every retrieved piece of evidence.

---

## 3. Data Flow Verification
Every query follows a deterministic, unidirectional data path:
$$\text{Query} \xrightarrow{\text{Embed}} \vec{q} \xrightarrow{\text{FAISS Top-}K} \{C_1, C_2, C_3\} \xrightarrow{\text{Prompt Injection}} \text{LLM} \xrightarrow{\text{Synthesis}} \text{Response} + \text{Citations}$$

This guarantees zero data leaks and ensures all generated answers are fully verifiable.

