from uuid import UUID

from pydantic import BaseModel


class WriteOff(BaseModel):
    id: UUID
    unit_name: str
    remaining_minutes: int
    ingredient_name: str

    @property
    def is_expired(self) -> bool:
        return self.remaining_minutes <= 0
