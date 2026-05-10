from pydantic import BaseModel, Field


class AirportResponse(BaseModel):

    id: int

    code: str = Field(
        ...,
        examples=["GRU"]
    )

    name: str = Field(
        ...,
        examples=["Aeroporto Internacional de Guarulhos"]
    )

    city: str = Field(
        ...,
        examples=["São Paulo"]
    )

    country: str = Field(
        ...,
        examples=["Brasil"]
    )


class AirportCreateRequest(BaseModel):

    code: str = Field(
        min_length=3,
        max_length=10
    )

    name: str = Field(
        min_length=3,
        max_length=255
    )

    city: str = Field(
        min_length=2,
        max_length=255
    )

    country: str = Field(
        min_length=2,
        max_length=255
    )