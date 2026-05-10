from fastapi import FastAPI
from fastapi.responses import JSONResponse

from shared.exceptions.business_exceptions import (
    ResourceNotFoundError,
    ValidationError,
    BusinessRuleError
)

from shared.exceptions.concurrency_exceptions import (
    ConcurrencyConflictError,
    OverbookingError,
    RoomUnavailableError
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(ResourceNotFoundError)
    async def not_found_handler(_, exc):

        return JSONResponse(
            status_code=404,
            content={
                "error": exc.message
            }
        )

    @app.exception_handler(ValidationError)
    async def validation_handler(_, exc):

        return JSONResponse(
            status_code=400,
            content={
                "error": exc.message
            }
        )

    @app.exception_handler(BusinessRuleError)
    async def business_rule_handler(_, exc):

        return JSONResponse(
            status_code=422,
            content={
                "error": exc.message
            }
        )

    @app.exception_handler(ConcurrencyConflictError)
    async def concurrency_handler(_, exc):

        return JSONResponse(
            status_code=409,
            content={
                "error": exc.message
            }
        )

    @app.exception_handler(OverbookingError)
    async def overbooking_handler(_, exc):

        return JSONResponse(
            status_code=409,
            content={
                "error": exc.message
            }
        )

    @app.exception_handler(RoomUnavailableError)
    async def room_handler(_, exc):

        return JSONResponse(
            status_code=409,
            content={
                "error": exc.message
            }
        )

    @app.exception_handler(Exception)
    async def generic_handler(_, exc):

        return JSONResponse(
            status_code=500,
            content={
                "error": "Erro interno do servidor",
                "details": str(exc)
            }
        )