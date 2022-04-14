from pykson import JsonObject, StringField, IntegerField


class jsonlogin(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()
    sessionid = StringField()
