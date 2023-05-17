from pydantic import BaseModel
from typing import Optional

class ConnectionPlantsAnimalsInBD(BaseModel):
    connection_plant_id: int
    connection_animal_id: int