from marshmallow import Schema, fields


class ConnectionSoilsPlantsOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class ConnectionSoilsPlantsInputSchemaDelete(Schema):
    connection_soils_plants_id = fields.Int(description="connection_soils_plants_id", required=True, example=1)
class ConnectionSoilsPlantsOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsPlantsErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsPlantsInputSchemaInsert(Schema):
    connection_soil_id = fields.Int(description="connection_soil_id", required=True, example=1)
    connection_plant_id = fields.Int(description="connection_plant_id", required=True, example=1)
    connection_soils_plants_isGood = fields.Bool(description="connection_soils_plants_isGood", required=True, example=True)
class ConnectionSoilsPlantsOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsPlantsErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsPlantsInputSchemaUpdateSoilID(Schema):
    connection_soils_plants_id = fields.Int(description="connection_soils_plants_id", required=True, example=1)
    connection_soil_id = fields.Int(description="connection_soil_id", required=True, example=1)
class ConnectionSoilsPlantsOutputSchemaUpdateSoilID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsPlantsErrorSchemaUpdateSoilID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsPlantsInputSchemaUpdatePlantID(Schema):
    connection_soils_plants_id = fields.Int(description="connection_soils_plants_id", required=True, example=1)
    connection_plant_id = fields.Int(description="connection_plant_id", required=True, example=1)
class ConnectionSoilsPlantsOutputSchemaUpdatePlantID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsPlantsErrorSchemaUpdatePlantID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsPlantsInputSchemaUpdateIsGood(Schema):
    connection_soils_plants_id = fields.Int(description="connection_soils_plants_id", required=True, example=1)
    connection_soils_plants_isGood = fields.Bool(description="connection_soils_plants_isGood", required=True, example=True)
class ConnectionSoilsPlantsOutputSchemaUpdateIsGood(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsPlantsErrorSchemaUpdateIsGood(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')
