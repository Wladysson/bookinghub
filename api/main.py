from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from shared.middleware.logging_middleware import LoggingMiddleware
from shared.middleware.error_handler import register_exception_handlers

from modules.airports.routes import (
    router as airports_router
)

from modules.flights.routes import (
    router as flights_router
)

from modules.hotels.routes import (
    router as hotels_router
)

from modules.reservations.routes import (
    router as reservations_router
)

from modules.payments.routes import (
    router as payments_router
)

from modules.customers.routes import (
    router as customers_router
)

from modules.reports.routes import (
    router as reports_router
)

from modules.recommendations.routes import (
    router as recommendations_router
)

from modules.pricing.routes import (
    router as pricing_router
)

app = FastAPI(
    title="BookingHub API",
    version="1.0.0",
    description="Plataforma de reservas com alta concorrência"
)

# MIDDLEWARES

app.add_middleware(LoggingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# EXCEPTION HANDLERS

register_exception_handlers(app)

# ROUTERS

app.include_router(
    airports_router
)

app.include_router(
    flights_router
)

app.include_router(
    hotels_router
)

app.include_router(
    reservations_router
)

app.include_router(
    payments_router
)

app.include_router(
    customers_router
)

app.include_router(
    reports_router
)

app.include_router(
    recommendations_router
)

app.include_router(
    pricing_router
)

# HEALTH CHECK

@app.get("/health")
def health_check():

    return {
        "status": "ok",
        "service": "bookinghub-api"
    }