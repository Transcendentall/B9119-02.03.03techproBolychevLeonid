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
    plant_isFodder = fields.Bool(description="plant_isFodder", required=True, example=True)
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

class PlantInputSchemaUpdateIsFodder(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_isFodder = fields.Bool(description="plant_isFodder", required=True, example=True)
class PlantOutputSchemaUpdateIsFodder(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateIsFodder(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateIsExactingToTheLight(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_isExactingToTheLight = fields.Bool(description="plant_isExactingToTheLight", required=True, example=True)
class PlantOutputSchemaUpdateIsExactingToTheLight(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateIsExactingToTheLight(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateIsOneYear(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_isOneYear = fields.Bool(description="plant_isOneYear", required=True, example=True)
class PlantOutputSchemaUpdateIsOneYear(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateIsOneYear(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateIsTwoYears(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_isTwoYears = fields.Bool(description="plant_isTwoYears", required=True, example=True)
class PlantOutputSchemaUpdateIsTwoYears(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateIsTwoYears(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateIsManyYears(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_isManyYears = fields.Bool(description="plant_isManyYears", required=True, example=True)
class PlantOutputSchemaUpdateIsManyYears(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateIsManyYears(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateClimat(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_climat = fields.Str(description="plant_climat", required=True, example='test')
class PlantOutputSchemaUpdateClimat(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateClimat(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateRequiredMineralsAndTraceElements(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_required_minerals_and_trace_elements = fields.Str(description="plant_required_minerals_and_trace_elements", required=True, example='test')
class PlantOutputSchemaUpdateRequiredMineralsAndTraceElements(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateRequiredMineralsAndTraceElements(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateTemperatureMin(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_temperature_min = fields.Int(description="plant_temperature_min", required=True, example=1)
class PlantOutputSchemaUpdateTemperatureMin(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateTemperatureMin(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateTemperatureMax(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_temperature_max = fields.Int(description="plant_temperature_max", required=True, example=1)
class PlantOutputSchemaUpdateTemperatureMax(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateTemperatureMax(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateKingdom(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_kingdom = fields.Str(description="plant_kingdom", required=True, example='test')
class PlantOutputSchemaUpdateKingdom(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateKingdom(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdatePhilum(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_philum = fields.Str(description="plant_philum", required=True, example='test')
class PlantOutputSchemaUpdatePhilum(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdatePhilum(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateClass(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_class = fields.Str(description="plant_class", required=True, example='test')
class PlantOutputSchemaUpdateClass(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateClass(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateOrder(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_order = fields.Str(description="plant_order", required=True, example='test')
class PlantOutputSchemaUpdateOrder(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateOrder(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateFamily(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_family = fields.Str(description="plant_family", required=True, example='test')
class PlantOutputSchemaUpdateFamily(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateFamily(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateGenus(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_genus = fields.Str(description="plant_genus", required=True, example='test')
class PlantOutputSchemaUpdateGenus(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateGenus(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdateSpecies(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_species = fields.Str(description="plant_species", required=True, example='test')
class PlantOutputSchemaUpdateSpecies(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdateSpecies(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class PlantInputSchemaUpdatePicture(Schema):
    plant_id = fields.Int(description="plant_id", required=True, example=1)
    plant_picture = fields.Str(description="plant_picture", required=True, example='test')
class PlantOutputSchemaUpdatePicture(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class PlantErrorSchemaUpdatePicture(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')
