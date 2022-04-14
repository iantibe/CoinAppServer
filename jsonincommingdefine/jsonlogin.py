from pykson import JsonObject, StringField


class jsonlogin(JsonObject):
    username = StringField()
    password = StringField()
