from pydantic import BaseModel, Field

class EnrichedLead(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    company: str = Field(..., min_length=1, max_length=120)
    message: str = Field(..., min_length=1, max_length=2500)
    qualification_status: str = Field(...,min_length=1, max_length=50)
    score: int = Field(..., ge=0, le=100)
    priority: str = Field(..., min_length=1, max_length=20)
    reason: str = Field(..., min_length=1, max_length=2500)
    suggested_action: str = Field(..., min_length=1, max_length=500)
