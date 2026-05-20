from modules.pricing.rules import (
    HIGH_SURGE_MULTIPLIER,
    MEDIUM_SURGE_MULTIPLIER,
    LOW_SURGE_MULTIPLIER
)


def get_surge_multiplier(demand_level: str) -> float:

    if demand_level == "HIGH":
        return HIGH_SURGE_MULTIPLIER

    if demand_level == "MEDIUM":
        return MEDIUM_SURGE_MULTIPLIER

    return LOW_SURGE_MULTIPLIER