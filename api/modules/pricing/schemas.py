from pydantic import BaseModel
from decimal import Decimal


class DynamicPricingResponse(BaseModel):
    flight_id: int
    base_price: Decimal
    occupancy_rate: float
    demand_level: str
    surge_multiplier: float
    final_price: Decimal