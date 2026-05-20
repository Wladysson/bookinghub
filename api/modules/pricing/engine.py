from decimal import Decimal

from modules.pricing.demand_analysis import (
    calculate_occupancy_rate,
    classify_demand
)

from modules.pricing.surge_calculator import (
    get_surge_multiplier
)


class PricingEngine:

    @staticmethod
    def calculate_dynamic_price(flight: dict):

        occupancy_rate = calculate_occupancy_rate(
            flight["total_seats"],
            flight["available_seats"]
        )

        demand_level = classify_demand(occupancy_rate)

        surge_multiplier = get_surge_multiplier(demand_level)

        final_price = (
            Decimal(str(flight["price"])) *
            Decimal(str(surge_multiplier))
        )

        return {
            "flight_id": flight["id"],
            "base_price": flight["price"],
            "occupancy_rate": occupancy_rate,
            "demand_level": demand_level,
            "surge_multiplier": surge_multiplier,
            "final_price": round(final_price, 2)
        }