from APIBase import APIBase
from Constants import Constants
from DatabaseComponents import DatabaseComponents
from DatabaseLogon import DatabaseLogon
from GenerateDataObjectComponent import GenerateDataObjectComponent
from GenerateJson import GenerateJson
from Logger import Logger
from exceptions.MultipleSessionsFound import MultipleSessionsFound
from exceptions.NoSessionFound import NoSessionFound
from jsonresponsedefine.jsonlogout import jsonlogout as jsonlogout_response
from jsonincommingdefine.jsonlogout import jsonlogout as jsonlogout_input


class APILogout(APIBase):

    def __init__(self, database: DatabaseLogon, log: Logger, generatejson: GenerateJson,  generatedataobjectcomponent: GenerateDataObjectComponent):
        super().__init__(database, log)
        self.generatedataobjectcomponent = generatedataobjectcomponent
        self.generatejson = generatejson

    def activate(self, json: str, authkey: str):
        try:
            if self.validatelogonsession(authkey) == False:
                self.logobject.info("Login authorization header " + authkey + " is invalid")
                return self.generatejson.generatejson(self._generatelogoutobject(Constants.SERVER_RESPONSE_INVALID_AUTHENTICATION_HEADER))
            datainput = self._generateLogoutDataobject(json)
            self.database.insertLogout(datainput.session)
            self.logobject.info(str(datainput.session) + " has logged out. Refer to database for exact time")
            return self.generatejson.generatejson(self._generatelogoutobject(Constants.SERVER_RESPONSE_OK))
        except NoSessionFound:
            return self.generatejson.generatejson(self._generatelogoutobject(Constants.SERVER_RESPONSE_USER_ALL_READY_LOGGED_OUT))
        except MultipleSessionsFound as e:
            self.logobject.exception(str(e))
            return self.generatejson.generatejson(self._generatelogoutobject(Constants.CUSTOMERRORMESSAGERESPONSECODE, "Multiple Sessions found. This error has been logged"))
        except Exception as e:
            self.logobject.exception(str(e))
            #TODO use above format is all error write to logger when using self.logobject.exception()
            return self.generatejson.generatejson(self._generatelogoutobject(Constants.CUSTOMERRORMESSAGERESPONSECODE, "Server Error. This error has been logged"))

    def _generatelogoutobject(self, statuscode, errormessage="unset"):
        responseobject = jsonlogout_response()
        responseobject.statuscode = statuscode
        responseobject.errormessage = errormessage
        return responseobject


    def _generateLogoutDataobject(self, js: str):
        return self.generatedataobjectcomponent.generateDataObject(js, jsonlogout_input)


if __name__ == '__main__':
    log = Logger()
    dbc = DatabaseComponents(log)
    dbl = DatabaseLogon(dbc, log)
    gj = GenerateJson()
    gdo = GenerateDataObjectComponent()
    logout = APILogout(dbl,log, gj, gdo)

    print(logout.activate({"session": "1b63009e-7fe2-45ff-a787-dc5a799248be"},"4-"))