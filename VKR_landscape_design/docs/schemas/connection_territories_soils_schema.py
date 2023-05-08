from marshmallow import Schema, fields


class ConnectionTerritoriesSoilsOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class ConnectionTerritoriesSoilsInputSchemaDelete(Schema):
    connection_territories_soils_id = fields.Int(description="connection_territories_soils_id", required=True, example=1)
class ConnectionTerritoriesSoilsOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionTerritoriesSoilsErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionTerritoriesSoilsInputSchemaInsert(Schema):
    connection_territorie_id = fields.Int(description="connection_territorie_id", required=True, example=1)
    connection_soil_id = fields.Int(description="connection_soil_id", required=True, example=1)
class ConnectionTerritoriesSoilsOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionTerritoriesSoilsErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionTerritoriesSoilsInputSchemaUpdateTerritorieID(Schema):
    connection_territories_soils_id = fields.Int(description="connection_territories_soils_id", required=True, example=1)
    connection_territorie_id = fields.Int(description="connection_territorie_id", required=True, example=1)
class ConnectionTerritoriesSoilsOutputSchemaUpdateTerritorieID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionTerritoriesSoilsErrorSchemaUpdateTerritorieID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionTerritoriesSoilsInputSchemaUpdateSoilID(Schema):
    connection_territories_soils_id = fields.Int(description="connection_territories_soils_id", required=True, example=1)
    connection_soil_id = fields.Int(description="connection_soil_id", required=True, example=1)
class ConnectionTerritoriesSoilsOutputSchemaUpdateSoilID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionTerritoriesSoilsErrorSchemaUpdateSoilID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


