from config.database import get_connection


class AuthRepository:

    @staticmethod
    def create_user(name, email, hashed_password):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (
                name,
                email,
                hashed_password
            )
            VALUES (%s, %s, %s)
            RETURNING id, name, email
        """, (name, email, hashed_password))

        user = cursor.fetchone()

        conn.commit()

        cursor.close()
        conn.close()

        return user

    @staticmethod
    def find_by_email(email):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                id,
                name,
                email,
                hashed_password
            FROM users
            WHERE email = %s
        """, (email,))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        return user