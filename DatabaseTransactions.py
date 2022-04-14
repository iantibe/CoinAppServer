from datetime import datetime

from sqlalchemy.exc import NoResultFound

from DatabaseComponents import DatabaseComponents
from Logger import Logger
from Mintmark import Mintmark
from TranTypes import TranTypes
from databasedefinitions.DatabaseDefinitions import CoinDefinition, TransactionsDefinition, TransactionTypeDefinition, \
    CoinTypesDefinition, CoinLocationDefinition, CoinSubLocationDefinition, UsersDefinition, SourceDefinition,SessionsDefinition


class DatabaseTransactions:

    def __init__(self, dbc: DatabaseComponents, log: Logger):
        self.database = dbc
        self.logger = log.genereatelogger(__name__)

    def insertCoinAndTransaction(self, tranamount: float, tranactiondate: datetime, year: int, mintmark: Mintmark, coinid: int,
                                 coincondition: str, cointypeid: int, locationid: int, sublocationid: int, sessionid: str,
                                 sourceid: int, note: str, receipt: int, trantype: TranTypes):
        try:
            tran = TransactionsDefinition()
            coin = CoinDefinition()
            coin.year = year
            coin.mintmark = mintmark
            coin.coinid = coinid
            coin.coincondition = coincondition

            #this four are not in the message signiture
            coin.notes = coinnotes
            coin.slabbarcode = slabbarcode
            coin.obversepic = obversepic
            coin.reversepic = reversepic
            #end

            tran.amount = tranamount
            tran.actiondate = tranactiondate
            tran.note = note
            tran.receipt = receipt

            session = self.database.genereateSession()
            cointypeidobject = session.query(CoinTypesDefinition).get(cointypeid)
            locationidobject = session.query(CoinLocationDefinition).get(locationid)
            sublocationidobject = session.query(CoinSubLocationDefinition).get(sublocationid)

            userobject = session.query(UsersDefinition).join(SessionsDefinition).filter(SessionsDefinition.sessionguid == sessionid).one()
            sourceidobject = session.query(SourceDefinition).get(sourceid)
            trantypeidobject = session.query(TransactionTypeDefinition).filter(
                TransactionTypeDefinition.trantype == trantype.name).one()
            coin.cointypes = cointypeidobject
            coin.coinlocation = locationidobject
            coin.coinsublocation = sublocationidobject
            coin.users = userobject
            tran.source = sourceidobject
            tran.trantype = trantypeidobject
            coin.transactions = [tran]
            session.add(coin)
            session.commit()
            self.logger.info("Coinid " + str(coin.coinid) + " and transaction added")
       #TODO add noresults found exception for the .one lines
        finally:
            session.close()

    def insertTransactions(self, coinprimarykey: int, amount: float, date: datetime, note: str, receipt: int, sourceid: int,
                           trantype: TranTypes):
        try:
            tran = TransactionsDefinition()
            session = self.database.genereateSession()
            coin = session.query(CoinDefinition).get(coinprimarykey)
            source = session.query(SourceDefinition).get(sourceid)
            tran.amount = amount
            tran.actiondate = date
            tran.note = note
            tran.receipt = receipt
            tran.source = source
            trantypeobject = session.query(TransactionTypeDefinition).filter(
                TransactionTypeDefinition.trantype == trantype.name).one()
            tran.trantype = trantypeobject
            coin.transactions.append(tran)

            session.add(coin)
            session.commit()
            self.logger.info("Transaction for coin id: " + str(coinid) + " added")
        finally:
            session.close()


if __name__ == '__main__':
    log = Logger()
    log2 = Logger()
    test = DatabaseTransactions(DatabaseComponents(log), log2)

    # problem with above


    # result = test.getTransactionTypeObject("Buy")
    # print(result.trantypeid)
    #test.insertTransactions(27, 34.54, datetime.now(), "note", 5, 1, TranTypes.gift)
    test.insertCoinAndTransaction(45.36,datetime.now(),45,Mintmark.S.name,1,"ms45",1,1,1,"205de6bd-bfb3-4953-b8c1-2fe3200fefd6",1,"note",1, TranTypes.gift)
