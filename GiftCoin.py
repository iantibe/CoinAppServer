from datetime import datetime

from Transaction_Action_Base import Transaction_Action_Base
from databasedefinitions.DatabaseDefinitions import TransactionsDefinition, CoinDefinition


class GiftCoin(Transaction_Action_Base):

   def __init__(self,coinid: int, coinnotes: str, mintmark: Mintmark, coincondition, reversepic, obversepic, coinyear: int, slabbarcode: str, note: str, amount: float, date: datetime, receipt: int):
       super().__init__(note, amount, date, receipt)
       self.coin = coin
       coin.coinid = coinid
       coin.mintmark = mintmark
       coin.coincondition = coincondition
       coin.obversepic = obversepic
       coin.reversepic = reversepic
       coin.year = coinyear
       coin.slabbarcode = slabbarcode
       coin.notes = coinnotes
