from pydantic import BaseModel
from typing import Optional


class RecommendationQuery(BaseModel):
    customer_id: int
    destination: Optional[str] = None
    max_price: Optional[float] = None