from pykson import JsonObject, StringField

class jsoncreatenewuser(JsonObject):
    firstname = StringField()
    lastname = StringField()
    password = StringField()
    username = StringField()
