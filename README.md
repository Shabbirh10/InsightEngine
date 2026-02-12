# InsightEngine: Knowledge Retreival Assistant

A "Research Assistant" platform leveraging Advanced RAG and Multimodal AI.

Screenshots
<img width="1466" height="734" alt="Screenshot 2026-02-12 at 12 44 27 PM" src="https://github.com/user-attachments/assets/ffd1174f-f748-4897-aa0d-86eabd670868" />

<img width="1466" height="734" alt="Screenshot 2026-02-12 at 12 48 59 PM" src="https://github.com/user-attachments/assets/e7615dd5-ca56-4e45-a30d-ae8b3e73d85d" />

=======
# 🎯 InsightEngine: A Knowledge Retrieval Assistant

> *Your personal research intern, powered by Gemini and Advanced RAG.*
>>>>>>> 1a5cbb0 (Rename project to InsightEngine and update README with human-like tone)

InsightEngine is more than just a document viewer. It’s a platform designed for researchers, students, and curious minds who want to **talk to their documents** instead of just reading them. Whether you're scanning a 200-page academic paper or just curious about a specific detail in a user manual, InsightEngine helps you find the needle in the haystack instantly.

## ✨ Why I Built This
Most document storage systems are passive. You upload a PDF, and it just sits there. I wanted to build something **active**—a system that understands context, handles images as well as text, and provides cited answers so you can verify the truth.

## 🚀 Key Features

### 1. 🔍 Advanced RAG (Retrieval-Augmented Generation)
We don't just send your entire document to an LLM (which is expensive and slow). We use a hybrid search strategy:
*   **Semantic Search:** Finds meaning even if the keywords don't match.
*   **Keyword Matching:** Ensures specific terms aren't missed.
*   *Result:* Precise, context-aware answers in seconds.

### 2. 👁️ Multimodal Intelligence
Powered by **Gemini 1.5 Pro**, InsightEngine isn't blind. 
*   It can "see" charts and images within your documents.
*   Visual search allows you to ask questions about diagrams and covers.

### 3. ✍️ Writing Coach Mode
Need to summarize a complex topic for a blog? Or critique your own writing style? The built-in Writing Coach agent analyzes your retrieved knowledge and helps you articulate it better.

## 🛠️ Technical Breakdown

*   **Brain:** Gemini 1.5 Pro (Massive 1M+ token context window).
*   **API Layer:** FastAPI (High-performance, asynchronous Python).
*   **Vector Engine:** ChromaDB (Local, privacy-first embedding storage).
*   **Frontend:** Streamlit (Clean, interactive dashboard).

## ⚡ Getting Started

1.  **Clone the Repo**
    ```bash
    git clone https://github.com/Shabbirh10/InsightEngine.git
    cd InsightEngine
    ```

2.  **Environment Setup**
    Create a `.env` file and add your Google API Key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    CHROMA_PERSIST_DIRECTORY=./chroma_db
    ```

3.  **Run the Platform**
    I've made it easy with a startup script:
    ```bash
    chmod +x run.sh
    ./run.sh
    ```
    This will spin up both the FastAPI backend (Port 8000) and the Streamlit UI (Port 8501).

## 🔮 Roadmap
- [ ] Integration with Pinecone for cloud-scale vector storage.
- [ ] Support for voice-to-query (Ask questions with your voice).
- [ ] GitHub Actions for automated RAG evaluation (using Ragas).

---
*Built by Shabbir Hardwarewala.*
