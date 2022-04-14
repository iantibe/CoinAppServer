from APIBase import APIBase
from Constants import Constants
from DatabaseComponents import DatabaseComponents
from DatabaseLogon import DatabaseLogon
from GenerateDataObjectComponent import GenerateDataObjectComponent
from GenerateJson import GenerateJson
from HashComponents import HashComponents
from HashPassword import HashPassword
from Logger import Logger
from jsonresponsedefine.jsoncreatenewuser import jsoncreatenewuser as jsoncreatenewuser_response
from jsonincommingdefine.jsoncreatenewuser import jsoncreatenewuser as jsoncreatenewuser_input




class APINewUser(APIBase):

    def __init__(self, database: DatabaseLogon, log: Logger, generatejson: GenerateJson, hash: HashPassword, generatedataobjectcomponent: GenerateDataObjectComponent):
        super().__init__(database, log)
        self.generatejson = generatejson
        self.hash = hash
        self.generatedataobjectcomponent = generatedataobjectcomponent

    def activate(self, json: str, authkey: str):
        try:
            if self.validatelogonsession(authkey) == False:
                self.logobject.info("Login authorization header " + authkey + " is invalid")
                return self.generatejson.generatejson(self._generatecreatenewuserobject(Constants.SERVER_RESPONSE_INVALID_AUTHENTICATION_HEADER))
            datainput = self._generateCreateNewUserDataObject(json)
            if self._checkUserExistsforNewUser(datainput.username):
                return self.generatejson.generatejson(self._generatecreatenewuserobject(Constants.SERVER_RESPONSE_EXISTING_USER))
            else:
                hashedpasswordforstorage = self.hash.generatePasswordBlockForStorage(datainput.password)
                self.database.insertNewUser(datainput.firstname, datainput.lastname,hashedpasswordforstorage,datainput.username)
                self.logobject.info("User " + datainput.username + " has been created")
                return self.generatejson.generatejson(self._generatecreatenewuserobject(Constants.SERVER_RESPONSE_OK))
        except Exception as e:
            self.logobject.exception(str(e))
            return self.generatejson.generatejson(self._generatecreatenewuserobject(Constants.CUSTOMERRORMESSAGERESPONSECODE, "A server error has occured. The problem has been logged"))

    def _generatecreatenewuserobject(self, statuscode, errormessage="unset"):
        responseobject = jsoncreatenewuser_response()
        responseobject.statuscode = statuscode
        responseobject.errormessage = errormessage
        return responseobject

    def _generateCreateNewUserDataObject(self, js: str):
        return self.generatedataobjectcomponent.generateDataObject(js, jsoncreatenewuser_input)

    def _checkUserExistsforNewUser(self, uname: str):
        # TODO changed this method; check here for problem if if it does not work
        result = self.database.checkDatabaseForExistingUserforNewUser(uname)
        if len(result) == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    log = Logger()
    dbc = DatabaseComponents(log)
    dbl = DatabaseLogon(dbc, log)
    gj = GenerateJson()
    gdo = GenerateDataObjectComponent()
    hashc = HashComponents()
    hash = HashPassword(hashc)
    logout = APINewUser(dbl,log,gj,hash,gdo)
    print(logout.activate({"firstname": "faith", "lastname": "tibe", "password": "toyotacar", "username": "ftibe"}, "4bbe7b23-1b5e-a9c0-f7c9fe0b234f"))
