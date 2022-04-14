from APIBase import APIBase
from DatabaseLogon import DatabaseLogon
from Logger import Logger
from Transaction import Transaction


class APIBuyCoin(APIBase):

    def __init__(self, database: DatabaseLogon, log: Logger, tran: Transaction):
        super().__init__(database, log)
        self.tran = tran
        self.loggerbuy = log.genereatelogger(__name__)


    def activate(self, json: str, authkey: str):

        pass