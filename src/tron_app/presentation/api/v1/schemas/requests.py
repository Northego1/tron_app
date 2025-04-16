import base58
from pydantic import BaseModel, Field, field_validator


class PostTronRequest(BaseModel):
    address: str = Field(examples=["TLBJML1LhqRePGBQVTmWFaTYeKgNpJwjKq"])

    @field_validator("address", mode="before")
    @classmethod
    def validate_address(cls, address: str) -> str:
        if not base58.b58decode_check(address).startswith(b"\x41"):
            raise ValueError("Invalid Tron address")
        return address
