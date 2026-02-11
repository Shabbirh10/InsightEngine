# The Intelligent Knowledge Platform: Smart Reader

A "Smart Netflix for Books/Docs" and "Research Assistant" platform leveraging Advanced RAG and Multimodal AI.

## System Architecture

```mermaid
graph TD
    User([User]) -->|Upload PDF/Image| API[FastAPI Backend]
    API -->|Process Text/Image| Gemini[Gemini 1.5 Pro]
    API -->|Store Embeddings| VectorDB[(ChromaDB / Pinecone)]
    API -->|Store Metadata| DB[(PostgreSQL / Supabase)]
    Gemini -->|Generate Embeddings| VectorDB
    User -->|Ask Question| API
    API -->|Retrieve Context| VectorDB
    API -->|Generate Answer| Gemini
    Gemini -->|Response| API
    API -->|Answer| User
```

## Features

1.  **Advanced RAG**: Hybrid search (semantic + keyword) for precise answers.
2.  **Multimodal Capabilities**: Visual search and cover scanning using Gemini 1.5 Pro.
3.  **Writing Coach Agent**: Smart editor for style critique based on genre.

## Tech Stack

-   **LLM / Brain**: Gemini 1.5 Pro (1M+ token context window).
-   **Backend**: FastAPI (High-performance ML API).
-   **Database**: Supabase / PostgreSQL (Metadata).
-   **Vector DB**: ChromaDB / Pinecone (Embeddings).

## Evaluation Metrics

We use Ragas / DeepEval to evaluate the RAG pipeline accuracy:
-   **Context Precision**: How relevant are the retrieved chunks?
-   **Answer Relevancy**: Does the generated answer address the query?
-   **Faithfulness**: Is the answer supported by the retrieved context?

## Live Demo

[Link to Live Demo (Coming Soon)]

## Setup

1.  Clone the repository.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Set up environment variables in `.env`.
4.  Run the backend: `uvicorn backend.main:app --reload`
