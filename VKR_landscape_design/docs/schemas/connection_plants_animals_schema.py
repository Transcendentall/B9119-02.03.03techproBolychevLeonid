from marshmallow import Schema, fields


class ConnectionPlantsAnimalsOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class ConnectionPlantsAnimalsInputSchemaDelete(Schema):
    connection_plants_animals_id = fields.Int(description="connection_plants_animals_id", required=True, example=1)
class ConnectionPlantsAnimalsOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionPlantsAnimalsErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionPlantsAnimalsInputSchemaInsert(Schema):
    connection_plant_id = fields.Int(description="connection_plant_id", required=True, example=1)
    connection_animal_id = fields.Int(description="connection_animal_id", required=True, example=1)
class ConnectionPlantsAnimalsOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionPlantsAnimalsErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionPlantsAnimalsInputSchemaUpdatePlantID(Schema):
    connection_plants_animals_id = fields.Int(description="connection_plants_animals_id", required=True, example=1)
    connection_plant_id = fields.Int(description="connection_plant_id", required=True, example=1)
class ConnectionPlantsAnimalsOutputSchemaUpdatePlantID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionPlantsAnimalsErrorSchemaUpdatePlantID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionPlantsAnimalsInputSchemaUpdateAnimalID(Schema):
    connection_plants_animals_id = fields.Int(description="connection_plants_animals_id", required=True, example=1)
    connection_animal_id = fields.Int(description="connection_animal_id", required=True, example=1)
class ConnectionPlantsAnimalsOutputSchemaUpdateAnimalID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionPlantsAnimalsErrorSchemaUpdateAnimalID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


