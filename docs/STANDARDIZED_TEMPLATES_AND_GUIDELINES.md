# Standardized Templates & Operational Guidelines

**Project:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 2 - Framework & Workflow Design  
**Author:** AI Ambassador & Engineering Intern  
**Classification:** Internal Engineering Standard Operating Procedure (SOP)  

---

## 1. Standard Prompt Templates

To enforce strict factual grounding and eliminate hallucinations, the assistant utilizes standardized prompt templates.

### 1.1 RAG System Prompt Template
```text
You are an expert technical knowledge assistant specializing in answering internal company documentation questions.

STRICT OPERATIONAL RULES:
1. Grounding Rule: Answer the question ONLY using the provided context snippets below.
2. Anti-Hallucination Rule: If the answer cannot be found in the context, explicitly state: "I cannot find sufficient information in the provided documentation to answer this question." Do not fabricate or extrapolate information.
3. Citation Rule: For every factual claim made in your response, provide the exact document name and section title in brackets, e.g., [Source: acme_cloud_overview.md - Section 3].
4. Tone & Style: Maintain an objective, concise, and professional engineering tone.
```

### 1.2 Retrieval Context Augmentation Template
```text
Context from documentation:
----------------------------------------
{context}
----------------------------------------

User Question: {question}

Helpful & Grounded Answer (with citations):
```

---

## 2. Text Chunking Guidelines & Mathematical Formula

### 2.1 Chunking Parameters
* **Primary Splitter:** `RecursiveCharacterTextSplitter`
* **Target Chunk Size ($C$):** 1,000 characters (~200 tokens)
* **Chunk Overlap ($O$):** 200 characters (~40 tokens)
* **Overlap Ratio:** $20\%$ of chunk size

### 2.2 Mathematical Formulas for Context Budgeting
For $N$ total characters in a document, the total number of chunks ($K_{total}$) is calculated by:
$$K_{total} = \left\lceil \frac{N - O}{C - O} \right\rceil$$

When retrieving $K=3$ chunks for context augmentation:
$$\text{Total Retrieved Tokens} \approx 3 \times 200 = 600 \text{ tokens}$$
This leaves ample headroom within the 128,000-token context window of `gpt-4o-mini`, guaranteeing fast response times and low API cost.

---

## 3. Document Ingestion Standard Operating Procedure (SOP)

When adding new documentation to the assistant, engineers must follow these steps:

1. **Format Validation:** Ensure files are formatted in valid Markdown (`.md`) with explicit Markdown headers (`#`, `##`, `###`) or clear PDF page breaks.
2. **Directory Placement:** Drop incoming files into the `data/sample_docs/` directory.
3. **Metadata Indexing:** LangChain loaders extract the document name and section headers as metadata attributes.
4. **Vector Store Refresh:** Re-run the embedding script or trigger the vector store update endpoint to re-index changed files without downtime.

---

## 4. Citation Formatting Standard

Every answer returned by the assistant must conclude with a standardized citation block:

```markdown
**Verified Sources & Citations:**
* **Document:** `acme_cloud_overview.md` | **Section:** 2. Authentication & API Keys
* **Document:** `acme_cloud_overview.md` | **Section:** 3. Webhook Delivery & Retry Policy
```
This guarantees 100% transparency so users can inspect the original source text directly.
