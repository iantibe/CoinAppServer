from pykson import JsonObject, StringField, IntegerField


class jsoncreatenewuser(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()
