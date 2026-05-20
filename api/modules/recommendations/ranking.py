def rank_recommendations(items: list, key: str = "recommendation_score"):

    return sorted(
        items,
        key=lambda item: item[key],
        reverse=True
    )