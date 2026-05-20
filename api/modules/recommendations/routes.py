from fastapi import APIRouter
from modules.recommendations.service import RecommendationService

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"]
)


@router.get("/{customer_id}")
def get_recommendations(customer_id: int):

    return RecommendationService.get_recommendations(customer_id)