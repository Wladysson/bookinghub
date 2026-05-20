from datetime import datetime


class AuditLog:
    def __init__(
        self,
        user_id,
        action,
        entity=None,
        entity_id=None,
        metadata=None,
        created_at=None
    ):
        self.user_id = user_id
        self.action = action
        self.entity = entity
        self.entity_id = entity_id
        self.metadata = metadata or {}
        self.created_at = created_at or datetime.utcnow()