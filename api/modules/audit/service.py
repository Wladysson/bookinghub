from modules.audit.repository import AuditRepository


class AuditService:

    @staticmethod
    def log_event(
        user_id,
        action,
        entity=None,
        entity_id=None,
        metadata=None
    ):
        return AuditRepository.create_log(
            user_id,
            action,
            entity,
            entity_id,
            metadata
        )

    @staticmethod
    def get_logs(limit=100):
        return AuditRepository.list_logs(limit)