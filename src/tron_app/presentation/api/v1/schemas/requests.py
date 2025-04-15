import base58
from pydantic import BaseModel, Field, field_validator


class PostTronRequest(BaseModel):
    address: str = Field(examples=["TWd413qHSXZ9ryAZUkk1A5j3PScT7jfahE"])

    @field_validator("address", mode="before")
    @classmethod
    def validate_address(cls, address: str) -> str:
        if not base58.b58decode_check(address).startswith(b"\x41"):
            raise ValueError("Invalid Tron address")
        return address



class Paginator(BaseModel):
    limit: int = Field(ge=0)
    offset: int = Field(ge=0)
