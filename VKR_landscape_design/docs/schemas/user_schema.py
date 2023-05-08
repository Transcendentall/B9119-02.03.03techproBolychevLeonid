from marshmallow import Schema, fields


class UserOutputSchema(Schema):
    result = fields.Int(description="Результат", required=True, example=25)


class UserInputSchemaGetOneUser(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
class UserOutputSchemaGetOneUser(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaGetOneUser(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')

class UserInputSchemaDelete(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
class UserOutputSchemaDelete(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaDelete(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaInsert(Schema):
    user_login = fields.Str(description="user_login", required=True, example='test')
    user_password = fields.Str(description="user_password", required=True, example='test')
    user_email = fields.Str(description="user_email", required=True, example='test')
class UserOutputSchemaInsert(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaInsert(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaAuthorisation(Schema):
    user_login = fields.Str(description="user_login", required=True, example='test')
    user_password = fields.Str(description="user_password", required=True, example='test')
class UserOutputSchemaAuthorisation(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaAuthorisation(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateLogin(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_login = fields.Str(description="user_login", required=True, example='test')
class UserOutputSchemaUpdateLogin(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateLogin(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdatePassword(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_password = fields.Str(description="user_password", required=True, example='test')
class UserOutputSchemaUpdatePassword(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdatePassword(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateEmail(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_email = fields.Str(description="user_email", required=True, example='test')
class UserOutputSchemaUpdateEmail(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateEmail(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateSurname(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_surname = fields.Str(description="user_surname", required=True, example='test')
class UserOutputSchemaUpdateSurname(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateSurname(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateName(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_name = fields.Str(description="user_name", required=True, example='test')
class UserOutputSchemaUpdateName(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateName(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateFathername(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_fathername = fields.Str(description="user_fathername", required=True, example='test')
class UserOutputSchemaUpdateFathername(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateFathername(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateAge(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_age = fields.Str(description="user_age", required=True, example='test')
class UserOutputSchemaUpdateAge(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateAge(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')



class UserInputSchemaUpdateIsFemale(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_isFemale = fields.Bool(description="user_isFemale", required=True, example=False)
class UserOutputSchemaUpdateIsFemale(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdateIsFemale(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdatePicture(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_picture = fields.Str(description="user_picture", required=True, example='test')
class UserOutputSchemaUpdatePicture(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaUpdatePicture(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')


class UserInputSchemaUpdateIsAdmin(Schema):
    user_id = fields.Int(description="user_id", required=True, example=1)
    user_isAdmin = fields.Bool(description="user_isAdmin", required=True, example=False)
class UserOutputSchemaIsAdmin(Schema):
    result = fields.Int(description="Результат", required=True, example=25)
class UserErrorSchemaIsAdmin(Schema):
    error = fields.Str(description="Сообщение об ошибке", required=True, example='Invalid input parameter number')