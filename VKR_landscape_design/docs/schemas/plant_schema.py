from marshmallow import Schema, fields


class PlantOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class PlantInputSchemaDelete(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
class PlantOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class PlantInputSchemaInsert(Schema):
    plant_name = fields.Str(description="plant_name", required=True, example='test')
    plant_description = fields.Str(description="plant_description", required=True, example='test')
    plant_isFodder = fields.Bool(description="plant_isFodder", required=True, example='True')
class PlantOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class PlantInputSchemaUpdateName(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_name = fields.Str(description="plant_name", required=True, example='test')
class PlantOutputSchemaUpdateName(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateName(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class PlantInputSchemaUpdateDescription(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_description = fields.Str(description="plant_description", required=True, example='test')
class PlantOutputSchemaUpdateDescription(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateDescription(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')