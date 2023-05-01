from marshmallow import Schema, fields


class GroundOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class GroundInputSchemaDelete(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
class GroundOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaInsert(Schema):
    ground_name = fields.Str(description="ground_name", required=True, example='test')
    ground_description = fields.Str(description="ground_description", required=True, example='test')
class GroundOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaUpdateName(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
    ground_name = fields.Str(description="ground_name", required=True, example='test')
class GroundOutputSchemaUpdateName(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaUpdateName(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaUpdateDescription(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
    ground_description = fields.Str(description="ground_description", required=True, example='test')
class GroundOutputSchemaUpdateDescription(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaUpdateDescription(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaUpdateDensity(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
    ground_density = fields.Str(description="ground_density", required=True, example='test')
class GroundOutputSchemaUpdateDensity(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaUpdateDensity(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaUpdateHumidity(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
    ground_humidity = fields.Str(description="ground_humidity", required=True, example='test')
class GroundOutputSchemaUpdateHumidity(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaUpdateHumidity(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaUpdateHardnessMoos(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
    ground_hardness_Moos = fields.Str(description="ground_hardness_Moos", required=True, example='test')
class GroundOutputSchemaUpdateHardnessMoos(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaUpdateHardnessMoos(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class GroundInputSchemaUpdatePicture(Schema):
    ground_id = fields.Int(description="ground_id", required=True, example=1)
    ground_picture = fields.Str(description="ground_picture", required=True, example='test')
class GroundOutputSchemaUpdatePicture(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class GroundErrorSchemaUpdatePicture(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')