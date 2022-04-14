from pykson import Pykson, JsonObject




class GenerateJson:
    #TODO add component to name to indicate a shared conmponent
    def __init__(self):
        pass

    def generatejson(self, jsonobject: JsonObject) -> str:
        return Pykson().to_json(jsonobject)



if __name__ == '__main__':
    test = GenerateJson()

    json = jsonvalidatesession()
    json.session = "fjsdklfja;sdfjskl"
    print(test.generatejson(json))
