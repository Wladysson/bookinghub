from dataclasses import dataclass
from typing import Optional


@dataclass
class Airport:

    id: Optional[int]
    code: str
    name: str
    city: str
    country: str