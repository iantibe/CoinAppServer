from APIBase import APIBase
from Constants import Constants
from DatabaseComponents import DatabaseComponents
from DatabaseLogon import DatabaseLogon
from GenerateDataObjectComponent import GenerateDataObjectComponent
from GenerateJson import GenerateJson
from HashComponents import HashComponents
from HashPassword import HashPassword
from Logger import Logger
from exceptions.DuplicateUserException import DuplicateUserException
from exceptions.NoPasswordBlockExistsForUser import NoPasswordBlockExistsForUser
from exceptions.NoUserExistsException import NoUserExistsException
from jsonresponsedefine.jsonlogin import jsonlogin as jsonlogin_response
from jsonincommingdefine.jsonlogin import jsonlogin as jsonlogin_input
from databasedefinitions.DatabaseDefinitions import UsersDefinition

class APILogin(APIBase):

    def __init__(self, database: DatabaseLogon, APIlogger: Logger, log: Logger, hash: HashPassword, generatejson: GenerateJson, generatedataobjectcomponent: GenerateDataObjectComponent):
        super().__init__(database, log)
        #TODO consolidate logger instances in the constructor
        self.hash = hash
        self.generatejson = generatejson
        self.generatedataobjectcomponent = generatedataobjectcomponent
        self.logobject = APIlogger.genereatelogger(__name__)

    def activate(self, json: str, authkey: str):
        # TODO this method will login a valid user in multiple times
        # TODO replace nubmers with string all methods in file

        try:
            if not self.validatelogonsession(authkey):
                self.logobject.info("Login authorization header " + authkey + " is invalid")
                return self.generatejson.generatejson(self._generateloginobject(Constants.SERVER_RESPONSE_INVALID_AUTHENTICATION_HEADER,"Invalid", "Unauthorized"))
            datainput = self._generateLoginDataobject(json)
            userid = self.database.checkDatabaseForUserExistForLogin(datainput.username)
            passwordblock = self.database.getPasswordBlock(userid)
            extractedpasswordfromstorage = self.hash.extractPasswordFromStorage(passwordblock)
            hashedinputpassword = self.hash.hashInputPassword(datainput.password, passwordblock)
            if extractedpasswordfromstorage == hashedinputpassword:
                sessionid = self.database.createSession(userid)
                self.logobject.info(str(sessionid) + " has logged on Refer to database for except time and date")
                return self.generatejson.generatejson(
                    self._generateloginobject(Constants.SERVER_RESPONSE_OK, str(sessionid)))

            else:
                self.logobject.info("User " + datainput.username + " input wrong password")
                return self.generatejson.generatejson(
                    self._generateloginobject(Constants.SERVER_RESPONSE_INVALID_PASSWORD, ""))
        except NoUserExistsException as e:

            return self.generatejson.generatejson(self._generateloginobject(1, ""))
        except DuplicateUserException as e:
            self.logobject.exception(str(e))
            return self.generatejson.generatejson(
                self._generateloginobject(Constants.CUSTOMERRORMESSAGERESPONSECODE, "", "Multiple Users with same name found. This error will be recorded"))
        except NoPasswordBlockExistsForUser as e:
            self.logobject.exception(str(e))
            return self.generatejson.generatejson(
                self._generateloginobject(Constants.CUSTOMERRORMESSAGERESPONSECODE, "", "No password exits for this user. This error will be recorded"))
        except Exception as e:
            self.logobject.exception(str(e))
            return self.generatejson.generatejson(
                self._generateloginobject(Constants.CUSTOMERRORMESSAGERESPONSECODE, "", "A server error occurred. This error will be recorded"))

    def _generateloginobject(self, statuscode, sessionid, errormessage="unset"):
        responseobject = jsonlogin_response()

        responseobject.statuscode = statuscode
        responseobject.sessionid = sessionid
        responseobject.errormessage = errormessage
        return responseobject

    def _generateLoginDataobject(self, js: str):
        return self.generatedataobjectcomponent.generateDataObject(js, jsonlogin_input)


if __name__ == '__main__':
    log = Logger()
    dbc = DatabaseComponents(log)
    dbl = DatabaseLogon(dbc, log)
    gj = GenerateJson()
    gdo = GenerateDataObjectComponent()
    hashc = HashComponents()
    hash = HashPassword(hashc)
    logout = APILogin(dbl, log,log,hash,gj,gdo)
    print(logout.activate({"username": "ftibe", "password": "toyotacar"}, "4bbe7b23-1b5e-44f6-a9c0-f7c9fe0b234f"))

