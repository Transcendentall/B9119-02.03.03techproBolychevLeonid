from marshmallow import Schema, fields

class TerritoriesInputSchema(Schema):
    id = fields.Int(description="id", required=True, example=1)

class TerritoriesOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)

class TerritoriesErrorSchema(Schema):
    error = fields.String(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

