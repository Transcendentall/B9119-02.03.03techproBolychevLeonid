# main.py

from typing import Optional
from controllers import UserController
from controllers import GroundController
from controllers import SoilController
from controllers import TerritorieController
from controllers import AnimalController
from controllers import PlantController
from controllers import ConnectionPlantsAnimalsController
from controllers import ConnectionSoilsPlantsController
from controllers import ConnectionSoilsGroundsController
from controllers import ConnectionTerritoriesSoilsController
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

app.include_router(UserController.router)
app.include_router(GroundController.router)
app.include_router(SoilController.router)
app.include_router(TerritorieController.router)
app.include_router(AnimalController.router)
app.include_router(PlantController.router)
app.include_router(ConnectionPlantsAnimalsController.router)
app.include_router(ConnectionSoilsPlantsController.router)
app.include_router(ConnectionSoilsGroundsController.router)
app.include_router(ConnectionTerritoriesSoilsController.router)
