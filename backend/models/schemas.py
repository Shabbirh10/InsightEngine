from pydantic import BaseModel
from typing import List, Optional

class URLUploadRequest(BaseModel):
    url: str

class TextUploadRequest(BaseModel):
    title: str
    content: str
    metadata: Optional[dict] = None

class QueryRequest(BaseModel):
    query: str
    n_results: int = 5

class QueryResponse(BaseModel):
    answer: str
    sources: List[dict]
