from fastapi import APIRouter

from modules.pricing.service import PricingService

router = APIRouter(
    prefix="/pricing",
    tags=["Dynamic Pricing"]
)


@router.get("/flight/{flight_id}")
def get_dynamic_flight_price(flight_id: int):

    return PricingService.get_dynamic_price(
        flight_id
    )