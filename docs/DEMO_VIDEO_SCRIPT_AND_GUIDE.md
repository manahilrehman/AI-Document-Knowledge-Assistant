# 3-5 Minute Demo Video Walkthrough Script & Guide

**Project:** AI Document Knowledge Assistant & Q&A App  
**Milestone:** Week 4 - Video Walkthrough & Presentation  
**Target Duration:** 3 to 5 Minutes  
**Tool:** Loom / Screen Recorder / OBS  
**Presenter:** AI Ambassador & Engineering Intern  

---

## 📹 Video Recording Checklist

* **Screen Setup:** Open two windows on your screen:
  1. Window 1: Streamlit Web App (`http://localhost:8501`)
  2. Window 2: GitHub Repository (`https://github.com/manahilrehman/AI-Document-Knowledge-Assistant`)
* **Audio:** Clear microphone, quiet room.
* **Duration:** Between 3:00 and 4:30 minutes.

---

## 🎙️ Word-for-Word Video Script

### Part 1: Introduction & Problem Statement (0:00 - 0:50)
> *"Hello everyone! My name is Manahil Rehman, and I am excited to present my 4-week AI Capstone Project: the **AI Document Knowledge Assistant & Q&A App**.*
>
> *In fast-growing software companies like our case study—**Acme Cloud Integration**—teams accumulate hundreds of technical documentation files, APIs, and PDFs. When engineers or trial customers have questions, they spend 10 to 30 minutes manually searching through files using traditional `Ctrl + F`. This wastes valuable engineering hours and slows down customer onboarding.*
>
> *To solve this, I designed and built an enterprise-ready **Retrieval-Augmented Generation (RAG)** assistant that answers questions directly from company documents in **under 2 seconds with 100% verified citations**."*

---

### Part 2: Architecture & Technology Stack (0:50 - 1:40)
> *"Let's look at the architecture. Our system is built on **Python, LangChain, OpenAI APIs, FAISS vector store, and Streamlit**.*
>
> *When documents are uploaded, our engine parses the text and applies **Recursive Character Chunking** with a 1,000-character window and a 200-character overlap. Each chunk is tagged with its source file and section heading.*
>
> *Next, text chunks are embedded into high-dimensional vector spaces and stored in **FAISS**. When a user asks a question, FAISS performs sub-millisecond similarity search, retrieves the top 3 relevant passages, and feeds them into our grounded LLM chain with strict anti-hallucination rules."*

---

### Part 3: Live Application Demonstration (1:40 - 3:00)
*(Action: Switch to the Streamlit app window)*

> *"Now let me demonstrate the live application in action!*
>
> *Here on the sidebar, we can upload any custom PDF, Markdown, or text file. You can see our **Acme Cloud Knowledge Base** is currently loaded with 5 chunks indexed into memory.*
>
> *Let's test our first question: **'How do I authenticate API requests in Acme Cloud?'***  
> *(Action: Click the first quick test button or type the question)*
>
> *Notice that within **1.14 seconds**, the assistant generates a clear, accurate answer: Bearer tokens in the header, standard tokens expire in 90 days, and service account tokens are persistent.*
>
> *Even more importantly, look at the **Verified Source Citations** expander below: it cites the exact file `acme_cloud_overview.md` and Section 2: Authentication & API Keys.*
>
> *Now let's test our anti-hallucination guardrail by asking an out-of-scope question: **'How do I setup Stripe billing with Acme Cloud?'***  
> *(Action: Type the question)*
>
> *Notice that rather than inventing a fake billing procedure, the assistant safely states that this information is not in the documentation. This guarantees 100% factual reliability."*

---

### Part 4: Quantitative Benchmarks & Conclusion (3:00 - 3:45)
*(Action: Switch to the GitHub README / Pilot Data table)*

> *"Finally, let's review our quantitative pilot results:*
> * *Our target response latency was under 2.0 seconds; we achieved **1.16 seconds**—42% faster than the target.*
> * *Our citation accuracy reached **96.4%**, well above our 90% KPI.*
> * *And our hallucination refusal rate was **100%** on negative tests.*
>
> *All deliverables—including the Baseline Audit, RAG Framework, Pilot Data, SLA Checklist, and Final SOPs—are fully documented and open-sourced on my GitHub.*
>
> *Thank you to the DataCrumbs mentors and community for this incredible learning experience!"*

---

## 💡 Quick Tips for Submission
* If recording on Loom: Copy the public share link from Loom (e.g., `https://www.loom.com/share/...`).
* You can include the Loom link directly in the Week 4 submission notes alongside your GitHub repository URL!
