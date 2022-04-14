from BuyCoin import BuyCoin
from DatabaseComponents import DatabaseComponents
from DatabaseTransactions import DatabaseTransactions
from GiftCoin import GiftCoin
from Logger import Logger
from LostCoin import LostCoin
from SellCoin import SellCoin
from TranTypes import TranTypes
from Transaction_Action_Base import Transaction_Action_Base
from databasedefinitions.DatabaseDefinitions import TransactionsDefinition
from databasedefinitions.DatabaseDefinitions import CoinDefinition

class Transaction:

    def __init__(self, databasetransactions: DatabaseTransactions):
        self.database = databasetransactions

    def transaction(self, input: Transaction_Action_Base) -> None:

        if not issubclass(type(input), Transaction_Action_Base):
            raise TypeError("Invalid input object")

        if isinstance(input, GiftCoin):
            self.database.insertCoinAndTransaction(0.00,input.transaction.actiondate,input.coin.year,input.coin.mintmark, input.coin.coinid,input.coin.coincondition,input.coin.typefk,input.coin.locationfk,input.coin.sublocationfk, input.coin.userfk,input.transaction.sourcefk,input.coin.notes,input.transaction.receipt, TranTypes.gift.name)
        elif isinstance(input, BuyCoin):
            self.database.insertCoinAndTransaction(input.transaction.amount,input.transaction.actiondate,input.coin.year,input.coin.mintmark,input.coin.coinid, input.coin.coincondition,input.coin.typefe, input.coin.locationfk,input.coin.sublocationfk,input.coin.userk, input.transaction.sourcefk,input.coin.notes, input.transaction.receipt, TranTypes.buy.name)

        elif isinstance(input, SellCoin):
            self.database.insertTransactions(input.coinid,input.transaction.amount,input.transaction.actiondate,input.transaction.note,input.transaction.receipt,input.transaction.sourcefk,TranTypes.sell.name)
        elif isinstance(input, LostCoin):
            self.database.insertTransactions(input.coinid,input.transaction.amount,input.transaction.actiondate,input.transaction.note,input.transaction.receipt,input.transaction.sourcefk,TranTypes.lost.name)
        else:
            raise NotImplementedError("Option not implemented")

