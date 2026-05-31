from typing import List, Optional
from pydantic import BaseModel


class ReviewRequest(BaseModel):
    language: str
    code: str


class Issue(BaseModel):
    type: str
    severity: str
    message: str
    line: Optional[int] = None


class ReviewResponse(BaseModel):
    score: int
    complexity: str
    maintainability_index: Optional[float]
    issues: List[Issue]
    ai_feedback: str
    improved_code: str