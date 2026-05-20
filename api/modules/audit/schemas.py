from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class AuditLogCreate(BaseModel):
    user_id: int
    action: str
    entity: Optional[str] = None
    entity_id: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None


class AuditLogResponse(BaseModel):
    id: int
    user_id: int
    action: str
    entity: Optional[str]
    entity_id: Optional[int]
    metadata: Optional[Dict[str, Any]]
    created_at: datetime