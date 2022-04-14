from pykson import StringField, IntegerField, JsonObject

class jsonlogout(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()