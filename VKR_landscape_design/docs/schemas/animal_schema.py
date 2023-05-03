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


class AnimalInputSchemaUpdateKingdom(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_kingdom = fields.Str(description="animal_kingdom", required=True, example='test')
class AnimalOutputSchemaUpdateKingdom(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateKingdom(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdatePhilum(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_philum = fields.Str(description="animal_philum", required=True, example='test')
class AnimalOutputSchemaUpdatePhilum(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdatePhilum(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdateClass(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_class = fields.Str(description="animal_class", required=True, example='test')
class AnimalOutputSchemaUpdateClass(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateClass(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdateOrder(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_order = fields.Str(description="animal_order", required=True, example='test')
class AnimalOutputSchemaUpdateOrder(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateOrder(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdateFamily(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_family = fields.Str(description="animal_family", required=True, example='test')
class AnimalOutputSchemaUpdateFamily(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateFamily(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdateGenus(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_genus = fields.Str(description="animal_genus", required=True, example='test')
class AnimalOutputSchemaUpdateGenus(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateGenus(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdateSpecies(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_species = fields.Str(description="animal_species", required=True, example='test')
class AnimalOutputSchemaUpdateSpecies(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdateSpecies(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class AnimalInputSchemaUpdatePicture(Schema):
    animal_id = fields.Int(description="animal_id", required=True, example=1)
    animal_picture = fields.Str(description="animal_picture", required=True, example='test')
class AnimalOutputSchemaUpdatePicture(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class AnimalErrorSchemaUpdatePicture(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')
