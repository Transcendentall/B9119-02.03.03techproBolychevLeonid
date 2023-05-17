from pydantic import BaseModel
from typing import Optional

class ConnectionSoilsGroundsInBD(BaseModel):
    connection_soil_id: int
    connection_ground_id: int