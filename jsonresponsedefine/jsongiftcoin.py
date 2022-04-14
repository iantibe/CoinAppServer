from pykson import JsonObject, StringField, IntegerField


class jsongiftcoin(JsonObject):
    statuscode = IntegerField()
    errormessage = StringField()
