from pykson import JsonObject, StringField


class jsonlogout(JsonObject):
    session = StringField()