# Operational SLA & Quality Assurance Checklist

**Project:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 3 - Execution & Tool Integration  
**Author:** AI Ambassador & Engineering Intern  
**Standard:** Enterprise SaaS Tier-1 Operational SLA  

---

## 1. Service Level Agreements (SLAs)

| Service Dimension | Target SLA Commitment | Measurement Methodology | Enforcement Mechanism |
| :--- | :--- | :--- | :--- |
| **Response Latency** | **P95 < 2.0 Seconds** | High-resolution monotonic timers logged per user interaction. | Streaming token generation + efficient FAISS index retrieval. |
| **Service Availability** | **99.5% Uptime** | Web interface availability without unhandled process termination. | Streamlit session resilience and automated exception handlers. |
| **Citation Verifiability** | **≥ 90% Accuracy** | Human audit & automated string match against source chunks. | Mandatory bracketed citation formatting (`[Source: doc - section]`). |
| **Hallucination Rate** | **< 5% Tolerance** | Negative test query benchmarks. | Strict system prompt instruction: explicit refusal on missing data. |
| **Document Ingestion** | **< 3.0s per Document** | Time from file upload to vector index completion. | In-memory chunking and vector insertion. |

---

## 2. Quality Assurance (QA) Verification Checklist

### 2.1 Functional Readiness
- [x] **Document Parser:** Supports `.pdf`, `.md`, and `.txt` file parsing without memory leaks.
- [x] **Chunk Splitter:** Recursive character chunking maintains intact sentences and logical headers.
- [x] **Vector Store Indexing:** FAISS creates valid vector embeddings and persists metadata.
- [x] **Query Retrieval:** Top-3 nearest neighbors correctly retrieved based on cosine similarity.
- [x] **Citation Component:** UI renders expandable source citations containing document name and excerpt.

### 2.2 Boundary & Error Handling
- [x] **Empty Query Handling:** Interface rejects empty or whitespace-only queries cleanly.
- [x] **Out-of-Scope Queries:** Refusal response triggered gracefully without model hallucination.
- [x] **Unsupported File Types:** File uploader restricts inputs strictly to `.pdf`, `.md`, and `.txt`.
- [x] **API Key Fallback:** Graceful fallback to local semantic search mode if external API credentials are not supplied.

### 2.3 Data Privacy & Security
- [x] **In-Memory Volatility:** Ingested documents and vector representations reside in session memory and are not persisted to untrusted external storage.
- [x] **Credential Hygiene:** `.env` file excluded from version control via `.gitignore`.
- [x] **No Data Leaks:** API keys never exposed in browser logs or client-side Javascript.

---

## 3. Operational Sign-Off & Approvals

* **Milestone:** Week 3 Execution & Tool Integration
* **Quality Assurance Lead:** AI Ambassador & Engineering Intern
* **Readiness Assessment:** **APPROVED FOR FINAL DEPLOYMENT & SOP PRESENTATION (WEEK 4)**
