from uuid import UUID

from pydantic import BaseModel


class ErrorMessage(BaseModel):
    id: UUID
    code: str
