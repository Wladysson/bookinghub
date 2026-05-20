from pydantic import BaseModel
from decimal import Decimal
from typing import Optional


class FlightRecommendation(BaseModel):
    flight_id: int
    flight_number: str
    origin: str
    destination: str
    price: Decimal
    available_seats: int
    recommendation_score: float


class HotelRecommendation(BaseModel):
    hotel_id: int
    hotel_name: str
    city: str
    stars: int
    price_per_night: Decimal
    recommendation_score: float


class RecommendationResponse(BaseModel):
    customer_id: int
    recommended_flights: list[FlightRecommendation]
    recommended_hotels: list[HotelRecommendation]