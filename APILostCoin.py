from APIBase import APIBase
from DatabaseLogon import DatabaseLogon
from DatabaseTransactions import DatabaseTransactions
from GenerateDataObjectComponent import GenerateDataObjectComponent
from GenerateJson import GenerateJson
from Logger import Logger


class APILostCoin(APIBase):

    def __init__(self, database: DatabaseLogon, log: Logger, tran: DatabaseTransactions, generatejson: GenerateJson, generatedataobjectcomponent: GenerateDataObjectComponent):
        super().__init__(database, log)
        self.databasetran = tran
        self.apilogger = log.genereatelogger(__name__)
        self.generatejson = generatejson
        self.generatedataobjectcomponent = generatedataobjectcomponent

    def activate(self, json: str, authkey: str) -> None:
        pass