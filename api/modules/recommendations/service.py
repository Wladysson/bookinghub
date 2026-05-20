from modules.recommendations.repository import RecommendationRepository
from modules.recommendations.engine import RecommendationEngine
from modules.recommendations.ranking import rank_recommendations


class RecommendationService:

    @staticmethod
    def get_recommendations(customer_id: int):

        flights = RecommendationRepository.get_top_flights()
        hotels = RecommendationRepository.get_top_hotels()

        processed_flights = RecommendationEngine.process_flights(flights)
        processed_hotels = RecommendationEngine.process_hotels(hotels)

        ranked_flights = rank_recommendations(processed_flights)
        ranked_hotels = rank_recommendations(processed_hotels)

        return {
            "customer_id": customer_id,
            "recommended_flights": ranked_flights,
            "recommended_hotels": ranked_hotels
        }