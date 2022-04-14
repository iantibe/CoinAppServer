from pykson import JsonObject, StringField, IntegerField


class jsonlostcoin(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()