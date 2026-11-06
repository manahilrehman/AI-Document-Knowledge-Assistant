# Final Standard Operating Procedure (SOP): AI Document Knowledge Assistant

**Project:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 4 - Final Implementation, SOPs & Executive Presentation  
**Document Code:** SOP-AI-RAG-2026-V1  
**Classification:** Standard Operating Procedure (Operational Hand-off)  

---

## 1. Purpose & Scope
This Standard Operating Procedure defines the deployment, maintenance, document ingestion, and operational troubleshooting protocols for the **AI Document Knowledge Assistant & Q&A App**. It is designed for software engineers, IT administrators, and customer support leads.

---

## 2. System Architecture & Component Dependencies

* **Frontend UI:** Streamlit (`src/app.py`)
* **Vector Store & Retrieval:** In-memory FAISS Index with cosine similarity
* **Text Chunking Engine:** Recursive character chunking (1,000 characters with 200 overlap)
* **LLM & Embeddings:** OpenAI `text-embedding-3-small` and `gpt-4o-mini` (with local deterministic fallback mode)
* **Runtime Environment:** Python 3.10+

---

## 3. Routine Operations & Maintenance Procedures

### 3.1 Adding New Company Documents
When new documentation, policies, or manuals are released:
1. **File Format Check:** Convert documents to `.md` (Markdown), `.txt`, or `.pdf`.
2. **Directory Placement:** Save the files into the `data/sample_docs/` directory.
3. **UI Ingestion:** In the running Streamlit web app, open the left sidebar and drop files into the **"Upload Custom Docs"** uploader.
4. **Validation:** Ensure the sidebar metric shows `Total Indexed Chunks` has updated cleanly without memory exhaustion.

### 3.2 Starting & Stopping the Service
* **To Start the Application:**
  ```bash
  streamlit run src/app.py
  ```
* **To Stop the Application:**
  Press `Ctrl + C` in the running terminal instance.

---

## 4. Quality Assurance & Anti-Hallucination Guidelines

To ensure the assistant maintains 100% factual accuracy:
1. **Strict Context Adherence:** The prompt template mandates that if the answer does not exist in the retrieved context, the system must trigger an explicit refusal:  
   *"I cannot find sufficient information in the provided documentation to answer this question."*
2. **Citation Verification:** Every answer must display the source filename and section header inside the **"Verified Source Citations"** expandable container.
3. **Periodic Benchmark Audits:** Run the 10 pilot queries in `docs/PILOT_EXECUTION_DATA.md` weekly to verify response latency stays below the 2.0s SLA.

---

## 5. Troubleshooting Matrix

| Issue Symptom | Root Cause | Resolution Action |
| :--- | :--- | :--- |
| **"No documents loaded" warning** | Vector store has not been initialized. | Click "Reset / Reload Acme Cloud KB" in the left sidebar or upload a custom file. |
| **Response Latency > 2.0 seconds** | File chunks are too large or system network is throttled. | Check chunk size parameter (ensure $C \le 1000$) or switch to local retrieval mode. |
| **Blank Citation Box** | An out-of-scope question was submitted. | Expected behavior: Grounded refusal triggered to prevent hallucination. |
| **PDF Extraction Error** | Corrupted or password-protected PDF. | Re-export the PDF without password encryption and re-upload. |

---

## 6. Sign-off & Maintenance Approval
* **SOP Author:** AI Ambassador & Engineering Intern
* **Review Cadence:** Quarterly Review or upon model upgrade
* **Status:** Operational Hand-off Complete

