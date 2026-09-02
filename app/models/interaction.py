from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class Interaction(BaseModel):
    user_id: str
    product_id: str
    action: Literal["view", "purchase", "rate"]
    rating: Optional[int] = None
    timestamp: datetime
