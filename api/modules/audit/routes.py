from fastapi import APIRouter
from modules.audit.service import AuditService

router = APIRouter(
    prefix="/audit",
    tags=["Audit"]
)


@router.get("/logs")
def get_logs(limit: int = 100):
    return AuditService.get_logs(limit)