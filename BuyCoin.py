from datetime import datetime

from Transaction_Action_Base import Transaction_Action_Base
from databasedefinitions.DatabaseDefinitions import CoinDefinition
from databasedefinitions.DatabaseDefinitions import TransactionsDefinition


class BuyCoin(Transaction_Action_Base):

   def __init__(self,coinid: int, coinnotes: str, slabbarcode: str, coinyear: int, coincondition: str, obversepic, reversepic, coinmintmark: Mintmark, note: str, amount: float, date: datetime, receipt: int):
       super().__init__(note, amount, date, receipt)
       self.coin = coin
       coin.coinid = coinid
       coin.mintmark = mintmark
       coin.coincondition = coincondition
       coin.obversepic = obversepic
       coin.reversepic = reversepic
       coin.year = coinyear
       coin.slabbarcode =slabbarcode
       coin.notes = coinnotes
