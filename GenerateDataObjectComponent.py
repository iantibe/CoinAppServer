from pykson import Pykson

from jsonincommingdefine.jsonlogin import jsonlogin


class GenerateDataObjectComponent:

    def __init__(self):
        pass

    def generateDataObject(self, json: str, dataobject):
        return Pykson().from_json(json, dataobject)


if __name__ == '__main__':
    test = GenerateDataObjectComponent()
    print(test.generateDataObject({"username": "false", "password": "unset"}, jsonlogin).password)