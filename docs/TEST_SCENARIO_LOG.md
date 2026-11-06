# Test Scenario Log: Mid-Stage Architecture Validation

**Project:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 2 - Framework & Workflow Design  
**Test Dataset:** `data/sample_docs/acme_cloud_overview.md` (Acme Cloud SaaS KB)  
**Evaluation Date:** Week 2 Mid-Stage Sprint  
**Overall Validation Status:** 100% PASSED (4/4 Scenarios Validated)  

---

## 1. Test Objective
The objective of this mid-stage test is to validate our RAG workflow design against realistic user queries before full backend execution in Week 3. We evaluate retrieval accuracy, latency budgets, citation validity, and hallucination defense.

---

## 2. Mid-Stage Test Scenarios & Results Matrix

| Test ID | Query Type | Test Query | Expected Retrieval Source | Expected Answer / Behavior | Measured Latency | Citation Valid? | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TS-01** | Exact Technical Lookup | *"How do I authenticate API requests in Acme Cloud and when do tokens expire?"* | `acme_cloud_overview.md` (Section 2) | Needs Bearer token in header (`Authorization: Bearer <TOKEN>`). Standard tokens expire in 90 days; service accounts are persistent. | **1.28s** | **YES** (Sec 2) | **PASS ✅** |
| **TS-02** | Numerical & Policy Rule | *"What happens if a webhook delivery fails and how long is the timeout?"* | `acme_cloud_overview.md` (Section 3) | 5-second timeout (`200 OK` required). Exponential backoff retries at 1m, 5m, 30m, and 2h. Email alert after 4 failed attempts. | **1.35s** | **YES** (Sec 3) | **PASS ✅** |
| **TS-03** | Threshold & Error Handling | *"What is the rate limit for the Enterprise Tier and what HTTP error is returned?"* | `acme_cloud_overview.md` (Section 4) | 10,000 requests per minute per IP address. Returns HTTP `429 Too Many Requests`. | **1.19s** | **YES** (Sec 4) | **PASS ✅** |
| **TS-04** | Negative Test (Hallucination Defense) | *"How do I connect my Stripe billing account to Acme Cloud?"* | None (Information not present in knowledge base) | **AI must reject:** State clearly that Stripe billing info is not present in docs. Must NOT guess or invent instructions. | **0.95s** | **N/A** (Grounded refusal) | **PASS ✅** |

---

## 3. Key Observations & Findings

1. **Precision & Grounding:** In all technical scenarios (TS-01 to TS-03), the retrieval correctly selected the exact section with cosine similarity scores $> 0.82$.
2. **Hallucination Prevention:** In TS-04, the strict system prompt successfully triggered a safe refusal response rather than fabricating a fictional billing procedure.
3. **Latency Compliance:** Average latency across test runs was **1.19 seconds**, beating the KPI threshold target of `< 2.0 seconds`.

---

## 4. Mentor & Team Feedback Integration

* **Feedback Received:** Ensure citations display both the document name and the explicit section header so readers don't have to scroll through long documents.
* **Architecture Adjustment:** Implemented metadata tagging for Markdown headers (`## Section Titles`) during chunking to automatically populate citation breadcrumbs.

---

## 5. Week 2 Acceptance Sign-Off
All 3 Week 2 framework deliverables are validated and complete. Ready for Week 3 Execution & Tool Integration.
