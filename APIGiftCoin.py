from APIBase import APIBase
from DatabaseLogon import DatabaseLogon
from DatabaseTransactions import DatabaseTransactions
from Logger import Logger


class APIGiftCoin(APIBase):

    def __init__(self, database: DatabaseLogon, log: Logger, databasetran = DatabaseTransactions):
        super().__init__(database, log)
        self.loggergiftcoin = log.genereatelogger(__name__)
        self.databasetran = databasetran

    def activate(self, json: str, authkey: str):
        pass