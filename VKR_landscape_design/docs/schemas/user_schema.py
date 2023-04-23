from marshmallow import Schema, fields

class UserInputSchema(Schema):
    id = fields.Int(description="id", required=True, example=1)

class UserOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)

class UserErrorSchema(Schema):
    error = fields.String(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

