from modules.recommendations.scoring import (
    calculate_flight_score,
    calculate_hotel_score
)


class RecommendationEngine:

    @staticmethod
    def process_flights(flights):

        recommendations = []

        for flight in flights:

            popularity = 8.5
            availability = min(flight["available_seats"] / 100, 1)
            price_factor = 7.0

            score = calculate_flight_score(
                popularity,
                availability,
                price_factor
            )

            recommendations.append({
                "flight_id": flight["id"],
                "flight_number": flight["flight_number"],
                "origin": flight["origin_airport_code"],
                "destination": flight["destination_airport_code"],
                "price": flight["price"],
                "available_seats": flight["available_seats"],
                "recommendation_score": score
            })

        return recommendations

    @staticmethod
    def process_hotels(hotels):

        recommendations = []

        for hotel in hotels:

            popularity = 9.0
            price_factor = 7.5

            score = calculate_hotel_score(
                hotel["stars"],
                popularity,
                price_factor
            )

            recommendations.append({
                "hotel_id": hotel["id"],
                "hotel_name": hotel["name"],
                "city": hotel["city"],
                "stars": hotel["stars"],
                "price_per_night": 350.00,
                "recommendation_score": score
            })

        return recommendations