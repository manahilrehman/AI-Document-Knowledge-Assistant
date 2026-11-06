# Core Technical Framework & RAG Operational Architecture

**Project Title:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 2 - Framework & Workflow Design  
**Author:** AI Ambassador & Engineering Intern  
**Target Scenario:** Acme Cloud Integration (SaaS Technical Documentation)  
**Status:** Approved Technical Architecture Draft  

---

## 1. Executive Architecture Overview

The purpose of this framework is to establish an end-to-end, deterministic **Retrieval-Augmented Generation (RAG)** pipeline. Instead of relying on a language model's pre-trained memory (which produces hallucinations and lacks access to private docs), our architecture injects relevant, verified document snippets directly into the model's working memory at query time.

```
+--------------------------------------------------------------------------------------------------+
|                                  END-TO-END RAG ARCHITECTURE                                     |
+--------------------------------------------------------------------------------------------------+
|                                                                                                  |
|   [ Uploaded Documents ] (PDF / Markdown)                                                        |
|              │                                                                                   |
|              ▼                                                                                   |
|   [ Stage 1: Document Parsing & Text Cleaning ]                                                  |
|              │                                                                                   |
|              ▼                                                                                   |
|   [ Stage 2: Recursive Character Chunking ] (Size: 1000 chars, Overlap: 200 chars)              |
|              │                                                                                   |
|              ▼                                                                                   |
|   [ Stage 3: Embedding Pipeline ] (OpenAI text-embedding-3-small, 1536-dim)                      |
|              │                                                                                   |
|              ▼                                                                                   |
|   [ Stage 4: Vector Index Store ] (FAISS In-Memory / Local Index)                                |
|              ▲                                                                                   |
|              │ Cosine Similarity Search (Top-K = 3)                                              |
|              │                                                                                   |
|   [ User Query ] ──► [ Query Embedding ]                                                         |
|                             │                                                                    |
|                             ▼                                                                    |
|   [ Stage 5: Context Assembly & Prompt Synthesis ]                                               |
|              │ (Grounding Rules + Retrieved Context Chunks + User Query)                         |
|              ▼                                                                                   |
|   [ OpenAI gpt-4o-mini LLM ]                                                                     |
|              │                                                                                   |
|              ▼                                                                                   |
|   [ Final Verified Answer with Exact Source Citations ] (< 2.0s Latency)                         |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+
```

---

## 2. Detailed 5-Stage Operational Pipeline

### Stage 1: Ingestion & Document Parsing
* **Supported Formats:** Markdown (`.md`), Plain Text (`.txt`), and Adobe PDF (`.pdf`).
* **Ingestion Engine:** LangChain `UnstructuredMarkdownLoader` and `PyPDFLoader`.
* **Metadata Attachment:** Every ingested file is enriched with metadata tags:
  * `source`: Original filename (e.g., `acme_cloud_overview.md`).
  * `section_title`: Header or title of the section.
  * `page_number`: Document page index (for PDFs).

### Stage 2: Recursive Text Chunking
Long documents cannot be processed in a single prompt without losing precision. We utilize **RecursiveCharacterTextSplitter**:
* **Chunk Size:** 1,000 characters (~200 to 250 tokens).
* **Chunk Overlap:** 200 characters (~40 to 50 tokens).
* **Separators:** `["\n\n", "\n", " ", ""]` (splits on paragraphs first, then sentences, preserving natural semantic units).
* **Why Overlap Matters:** Overlapping prevents critical context from being cut in half between two neighboring chunks.

### Stage 3: Vector Embeddings
* **Model:** OpenAI `text-embedding-3-small`.
* **Vector Dimension:** 1,536 floating-point values per chunk.
* **Cost & Performance Efficiency:** `text-embedding-3-small` delivers higher retrieval performance at 1/5th the cost of legacy `text-embedding-ada-002`.

### Stage 4: Vector Store & Retrieval (FAISS)
* **Index Type:** FAISS (Facebook AI Similarity Search) IndexFlatL2 / IndexFlatIP (Cosine Similarity).
* **Search Strategy:** Top-K Nearest Neighbor Retrieval where `K = 3`.
* **Score Threshold:** Chunks with cosine similarity score `< 0.70` are filtered to avoid irrelevant noise.

### Stage 5: Context Injection & Synthesis
* The top-3 retrieved chunks are formatted into a clean context block.
* The prompt instructs the LLM (`gpt-4o-mini`) to synthesize the final answer **strictly** from the context.
* Citations are parsed and displayed in an expandable UI block below the answer.

---

## 3. Latency Budget Analysis

To meet the project KPI requirement of **Response Time < 2.0 Seconds**, each operational step is budgeted as follows:

| Operational Step | Target Latency | Optimization Mechanism |
| :--- | :--- | :--- |
| **1. Query Vectorization** | ~120 ms | OpenAI `text-embedding-3-small` lightweight API call. |
| **2. FAISS Similarity Search** | ~15 ms | In-memory indexing using matrix multiplication. |
| **3. Context Formatting & Prompt Prep** | ~10 ms | In-memory string templating. |
| **4. LLM Generation (gpt-4o-mini)** | ~1,200 ms | Streaming tokens with `temperature=0.0` for deterministic speed. |
| **Total Estimated Latency** | **~1,345 ms (< 1.4s)** | **Safely within the < 2.0s KPI boundary.** |

---

## 4. Architectural Failure Modes & Safeguards

1. **Failure Mode: Missing Information in Documents**
   * *Risk:* LLM invents a convincing but incorrect answer.
   * *Safeguard:* System prompt explicitly states: *"If the provided context does not contain the answer, reply with 'I cannot find this information in the provided documentation.' Do not attempt to guess."*

2. **Failure Mode: Conflicting Information Across Multiple Versions**
   * *Safeguard:* Metadata includes file modification timestamps. Retrieval ranks newer documents higher in similarity tie-breaks.
