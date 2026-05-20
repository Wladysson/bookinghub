from starlette.middleware.base import BaseHTTPMiddleware
from modules.audit.logger import log_event
import time


class AuditMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start = time.time()

        response = await call_next(request)

        duration = time.time() - start

        user_id = request.headers.get("X-User-ID")

        if user_id:
            log_event(
                user_id=int(user_id),
                action=f"{request.method} {request.url.path}",
                entity="http_request",
                metadata={
                    "status_code": response.status_code,
                    "duration": duration
                }
            )

        return response