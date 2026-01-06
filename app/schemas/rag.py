from pydantic import BaseModel
from typing import List, Optional

# Ingest 스키마
class NewsIngestRequest(BaseModel):
    title: str
    content: str
    published_at: Optional[str] = None
    url: Optional[str] = None

class IngestResponse(BaseModel):
    status: str
    doc_id: int
    chunks_count: int


# Chat 스키마
class ChatRequest(BaseModel):
    query: str
    user_id: Optional[str] = None

class SourceDocument(BaseModel):
    title: str
    content: str
    similarity: float

class ChatResponse(BaseModel):
    answer: str
    used_tools: List = [] # AI가 주가 조회했는지 뉴스검색 했는지
    sources: List[SourceDocument] = [] # 참고 문서들
    