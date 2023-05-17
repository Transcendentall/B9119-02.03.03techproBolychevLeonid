from pydantic import BaseModel
from typing import Optional

class PlantInBD(BaseModel):
    plant_name: str
    plant_description: str
    plant_isFodder: bool
    plant_isExactingToTheLight: Optional[bool] = None
    plant_isOneYear: Optional[bool] = None
    plant_isTwoYears: Optional[bool] = None
    plant_isManyYears: Optional[bool] = None
    plant_climat: Optional[str] = None
    plant_required_minerals_and_trace_elements: Optional[str] = None
    plant_temperature_min: Optional[int] = None
    plant_temperature_max: Optional[int] = None
    plant_kingdom: Optional[str] = None
    plant_philum: Optional[str] = None
    plant_class: Optional[str] = None
    plant_order: Optional[str] = None
    plant_family: Optional[str] = None
    plant_genus: Optional[str] = None
    plant_species: Optional[str] = None
    plant_picture: Optional[str] = None