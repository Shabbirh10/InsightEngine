from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.gemini_service import GeminiService
from backend.services.vector_db import VectorDBService
from backend.models.schemas import TextUploadRequest, QueryRequest, QueryResponse
import uuid
from pypdf import PdfReader
import io

router = APIRouter()
vector_service = VectorDBService()
gemini_service = GeminiService()

@router.post("/upload/text")
async def upload_text(request: TextUploadRequest):
    doc_id = str(uuid.uuid4())
    try:
        vector_service.add_document(doc_id, request.content, request.metadata)
        return {"message": "Document uploaded successfully", "doc_id": doc_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    try:
        pdf_reader = PdfReader(io.BytesIO(content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        
        doc_id = str(uuid.uuid4())
        vector_service.add_document(doc_id, text, {"filename": file.filename, "type": "pdf"})
        return {"message": "PDF uploaded successfully", "doc_id": doc_id, "filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

from tenacity import RetryError

@router.post("/query", response_model=QueryResponse)
async def query_documents(request: QueryRequest):
    try:
        # 1. Retrieve relevant chunks from Vector DB
        results = vector_service.query(request.query, request.n_results)
        
        # Extract text from results
        if not results['documents'] or not results['documents'][0]:
            return QueryResponse(answer="I couldn't find any relevant documents to answer your question.", sources=[])

        context_text = "\n\n".join(results['documents'][0])
        
        # 2. Augment prompt for Gemini
        prompt = f"""
        You are an intelligent knowledge assistant. Use the following context to answer the user's question.
        If the answer is not in the context, say you don't know.
        
        Context:
        {context_text}
        
        Question:
        {request.query}
        """
        
        # 3. Generate answer
        answer = gemini_service.generate_content(prompt)
        
        return QueryResponse(
            answer=answer,
            sources=[{"text": text} for text in results['documents'][0]]
        )
    except RetryError:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Please try again in 1 minute.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
