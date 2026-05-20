from config.database import get_connection
from psycopg2.extras import Json

class AuditRepository:

    @staticmethod
    def create_log(user_id, action, entity, entity_id, metadata):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO audit_logs (
                user_id,
                action,
                entity,
                entity_id,
                metadata
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id, user_id, action, entity, entity_id, metadata, created_at
        """, (
            user_id,
            action,
            entity,
            entity_id,
            Json(metadata)   # ✅ FIX AQUI
        ))

        log = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return log