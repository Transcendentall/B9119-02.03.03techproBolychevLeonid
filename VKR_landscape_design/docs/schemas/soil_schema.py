from marshmallow import Schema, fields


class SoilOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class SoilInputSchemaDelete(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
class SoilOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class SoilInputSchemaInsert(Schema):
    soil_name = fields.Str(description="soil_name", required=True, example='test')
    soil_description = fields.Str(description="soil_description", required=True, example='test')
class SoilOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class SoilInputSchemaUpdateName(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
    soil_name = fields.Str(description="soil_name", required=True, example='test')
class SoilOutputSchemaUpdateName(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaUpdateName(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class SoilInputSchemaUpdateDescription(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
    soil_description = fields.Str(description="soil_description", required=True, example='test')
class SoilOutputSchemaUpdateDescription(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaUpdateDescription(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class SoilInputSchemaUpdateAcidity(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
    soil_acidity = fields.Str(description="soil_acidity", required=True, example='test')
class SoilOutputSchemaUpdateAcidity(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaUpdateAcidity(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class SoilInputSchemaUpdateMinerals(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
    soil_minerals = fields.Str(description="soil_minerals", required=True, example='test')
class SoilOutputSchemaUpdateMinerals(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaUpdateMinerals(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class SoilInputSchemaUpdateProfile(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
    soil_profile = fields.Str(description="soil_profile", required=True, example='test')
class SoilOutputSchemaUpdateProfile(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaUpdateProfile(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class SoilInputSchemaUpdatePicture(Schema):
    soil_id = fields.Int(description="soil_id", required=True, example=1)
    soil_picture = fields.Str(description="soil_picture", required=True, example='test')
class SoilOutputSchemaUpdatePicture(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class SoilErrorSchemaUpdatePicture(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')