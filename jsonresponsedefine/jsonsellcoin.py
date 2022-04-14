from pykson import JsonObject, StringField, IntegerField

class jsonsellcoin(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()