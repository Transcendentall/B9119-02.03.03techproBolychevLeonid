from marshmallow import Schema, fields


class AnimalOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class AnimalInputSchemaDelete(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
class AnimalOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class AnimalInputSchemaInsert(Schema):
    animal_name = fields.Str(description="animal_name", required=True, example='test')
    animal_description = fields.Str(description="animal_description", required=True, example='test')
class AnimalOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class AnimalInputSchemaUpdateName(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_name = fields.Str(description="animal_name", required=True, example='test')
class AnimalOutputSchemaUpdateName(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateName(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class AnimalInputSchemaUpdateDescription(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_description = fields.Str(description="animal_description", required=True, example='test')
class AnimalOutputSchemaUpdateDescription(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateDescription(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')