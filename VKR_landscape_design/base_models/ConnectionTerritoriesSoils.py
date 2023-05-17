from pydantic import BaseModel
from typing import Optional

class ConnectionTerritoriesSoilsInBD(BaseModel):
    connection_territorie_id: int
    connection_soil_id: int