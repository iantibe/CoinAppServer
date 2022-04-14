from pykson import JsonObject, StringField, IntegerField


class jsonbuycoin(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()