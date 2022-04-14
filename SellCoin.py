from datetime import datetime

from Transaction_Action_Base import Transaction_Action_Base
from databasedefinitions.DatabaseDefinitions import TransactionsDefinition


class SellCoin(Transaction_Action_Base):

    def __init__(self, coinid: int, note: str, amount: float, date: datetime, receipt: int):
        super().__init__(note, amount, date, receipt)
        self.coinid = coinid
