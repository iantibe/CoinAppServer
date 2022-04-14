from APIBase import APIBase
from DatabaseLogon import DatabaseLogon
from DatabaseTransactions import DatabaseTransactions
from GenerateDataObjectComponent import GenerateDataObjectComponent
from GenerateJson import GenerateJson
from Logger import Logger
from jsonresponsedefine.jsonsellcoin import jsonsellcoin as jsonsellcoin_response


class APISellCoin(APIBase):

    def __init__(self, database: DatabaseLogon, log: Logger, databasetransaction: DatabaseTransactions, generatejson: GenerateJson, generatedataobjectcomponent: GenerateDataObjectComponent):
        super().__init__(database, log)
        self.logsellcoin = log.genereatelogger(__name__)
        self.databasetransaction = databasetransaction
        self.generatejson = generatejson
        self.generatedataobjectcomponent = generatedataobjectcomponent

    def activate(self, json: str, authkey: str):
        pass

    def _generatesellcoinobject(self, statuscode, errormessage="unset"):
        responseobject = jsonsellcoin_response()
        responseobject.statuscode = statuscode
        responseobject.errormessage = errormessage
        return responseobject


    def _generatesellcoinDataobject(self, js: str):
        return self.generatedataobjectcomponent.generateDataObject(js, jsonlogout_input)
