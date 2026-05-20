from modules.audit.service import AuditService


def log_event(
    user_id,
    action,
    entity=None,
    entity_id=None,
    metadata=None
):
    return AuditService.log_event(
        user_id=user_id,
        action=action,
        entity=entity,
        entity_id=entity_id,
        metadata=metadata
    )