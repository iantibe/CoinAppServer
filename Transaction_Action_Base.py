import datetime

from databasedefinitions.DatabaseDefinitions import TransactionsDefinition


class Transaction_Action_Base:

    def __init__(self, note: str, amount: float, date: datetime.datetime, receipt: int ):
        self.transaction = TransactionsDefinition()

        self.transaction.note = note
        self.transaction.amount = amount
        self.transaction.actiondate = date
        self.transaction.receipt = receipt