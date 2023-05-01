from marshmallow import Schema, fields


class TerritorieOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class TerritorieInputSchemaDelete(Schema):
    territorie_id = fields.Int(description="territorie_id", required=True, example=1)
class TerritorieOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class TerritorieErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class TerritorieInputSchemaInsert(Schema):
    territorie_coord_x = fields.Float(description="territorie_coord_x", required=True, example='1')
    territorie_coord_y = fields.Float(description="territorie_coord_y", required=True, example='1')
    territorie_coord_z = fields.Float(description="territorie_coord_z", required=True, example='1')
class TerritorieOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class TerritorieErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class TerritorieInputSchemaUpdateCoordX(Schema):
    territorie_id = fields.Int(description="territorie_id", required=True, example=1)
    territorie_coord_x = fields.Float(description="territorie_coord_x", required=True, example='1')
class TerritorieOutputSchemaUpdateCoordX(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class TerritorieErrorSchemaUpdateCoordX(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class TerritorieInputSchemaUpdateCoordY(Schema):
    territorie_id = fields.Int(description="territorie_id", required=True, example=1)
    territorie_coord_y = fields.Float(description="territorie_coord_y", required=True, example='1')
class TerritorieOutputSchemaUpdateCoordY(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class TerritorieErrorSchemaUpdateCoordY(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class TerritorieInputSchemaUpdateCoordZ(Schema):
    territorie_id = fields.Int(description="territorie_id", required=True, example=1)
    territorie_coord_z = fields.Float(description="territorie_coord_z", required=True, example='1')
class TerritorieOutputSchemaUpdateCoordZ(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class TerritorieErrorSchemaUpdateCoordZ(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')