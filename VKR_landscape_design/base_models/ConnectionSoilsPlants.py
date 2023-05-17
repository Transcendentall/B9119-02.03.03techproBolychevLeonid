from pydantic import BaseModel
from typing import Optional

class ConnectionSoilsPlantsInBD(BaseModel):
    connection_soil_id: int
    connection_plant_id: int
    connection_soils_plants_isGood: bool