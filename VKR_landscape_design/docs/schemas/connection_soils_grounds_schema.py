from marshmallow import Schema, fields


class ConnectionSoilsGroundsOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class ConnectionSoilsGroundsInputSchemaDelete(Schema):
    connection_soils_grounds_id = fields.Int(description="connection_soils_grounds_id", required=True, example=1)
class ConnectionSoilsGroundsOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsGroundsErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsGroundsInputSchemaInsert(Schema):
    connection_soil_id = fields.Int(description="connection_soil_id", required=True, example=1)
    connection_ground_id = fields.Int(description="connection_ground_id", required=True, example=1)
class ConnectionSoilsGroundsOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsGroundsErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsGroundsInputSchemaUpdateSoilID(Schema):
    connection_soils_grounds_id = fields.Int(description="connection_soils_grounds_id", required=True, example=1)
    connection_soil_id = fields.Int(description="connection_soil_id", required=True, example=1)
class ConnectionSoilsGroundsOutputSchemaUpdateSoilID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsGroundsErrorSchemaUpdateSoilID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class ConnectionSoilsGroundsInputSchemaUpdateGroundID(Schema):
    connection_soils_grounds_id = fields.Int(description="connection_soils_grounds_id", required=True, example=1)
    connection_ground_id = fields.Int(description="connection_ground_id", required=True, example=1)
class ConnectionSoilsGroundsOutputSchemaUpdateGroundID(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class ConnectionSoilsGroundsErrorSchemaUpdateGroundID(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


