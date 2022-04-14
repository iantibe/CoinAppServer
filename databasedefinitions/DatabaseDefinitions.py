from sqlalchemy import Column, ForeignKey, Enum, String, INT, DateTime, DATE, BINARY
from sqlalchemy.dialects.mysql import LONGBLOB, TINYINT, TEXT, CHAR, INTEGER, DECIMAL
from sqlalchemy.orm import relationship
from SqlalchemyBase import Base


class UsersDefinition(Base):
    __tablename__ = 'users'
    userid = Column(INTEGER(11), primary_key=True)
    firstname = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    password = Column(BINARY)
    username = Column(String(20))
    coins = relationship("CoinDefinition", backref="users")
    coinlocations = relationship("CoinLocationDefinition", backref="users")
    cointypes = relationship("CoinTypesDefinition", backref='users')
    sessions = relationship("SessionsDefinition", backref='users')
    sources = relationship("SourceDefinition", backref='users')

class TransactionTypeDefinition(Base):
    __tablename__ = 'trantype'
    trantypeid = Column(INTEGER(11), primary_key=True)
    trantype = Column(String(30), nullable=False)
    transactions = relationship("TransactionsDefinition", backref='trantype')



class TransactionsDefinition(Base):
    __tablename__ = 'transactions'
    id = Column(INTEGER(11), primary_key=True)
    coinfk = Column(ForeignKey('coin.id'), index=True, nullable=False)
    actiondate = Column(DATE, nullable=False)
    trantypefk = Column(ForeignKey('trantype.trantypeid'), index=True)
    amount = Column(DECIMAL(8, 2), nullable=False)
    note = Column(TEXT)
    receipt = Column(INTEGER(11))
    sourcefk = Column(ForeignKey('source.sourceid'), index=True)
    #coin = relationship('CoinDefinition')
    #source = relationship('SourceDefinition')
    #trantype = relationship('TransactionTypeDefinition')
    #coin = relationship("CoinDefinition", back_populates="transactions")

class SourceDefinition(Base):
    __tablename__ = 'source'
    sourceid = Column(INTEGER(11), primary_key=True)
    source = Column(String(30), nullable=False)
    userfk = Column(ForeignKey('users.userid'), index=True)
    #user = relationship("UsersDefinition")
    transactions = relationship("TransactionsDefinition", backref='source')


class SessionsDefinition(Base):
    __tablename__ = 'sessions'
    sessionid = Column(INTEGER(11), primary_key=True)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime)
    sessionguid = Column(String, nullable=False)
    usersfk = Column(ForeignKey('users.userid'), nullable=False, index=True)
    #user = relationship('UsersDefinition')


class CoinTypesDefinition(Base):
    __tablename__ = 'cointypes'
    typeid = Column(INTEGER(11), primary_key=True)
    type = Column(String(30))
    userfk = Column(ForeignKey('users.userid'), index=True)
    #user = relationship('UsersDefinition')
    coins = relationship("CoinDefinition", backref='cointypes')



class CoinLocationDefinition(Base):
    __tablename__ = 'coinlocation'
    locationid = Column(INTEGER(11), primary_key=True)
    location = Column(String(30), nullable=False)
    userfk = Column(ForeignKey('users.userid'), index=True)
    #user = relationship('UsersDefinition')
    coins = relationship("CoinDefinition", backref="coinlocation")



class CoinSubLocationDefinition(Base):
    __tablename__ = 'coinsublocation'
    sublocationid = Column(INTEGER(11), primary_key=True)
    locationfk = Column(ForeignKey('coinlocation.locationid'), index=True)
    sublocation = Column(String, nullable=False)
    #coinlocation = relationship('CoinLocationDefinition')
    coins = relationship("CoinDefinition", backref="coinsublocation")
    coinlocations = relationship("CoinLocationDefinition", backref='coinsublocation')

class CoinDefinition(Base):
    __tablename__ = 'coin'
    id = Column(INTEGER(11), primary_key=True)
    userfk = Column(ForeignKey('users.userid'), index=True)
    typefk = Column(ForeignKey('cointypes.typeid'), index=True, nullable=False)
    locationfk = Column(ForeignKey('coinlocation.locationid'), index=True)
    sublocationfk = Column(ForeignKey('coinsublocation.sublocationid'), index=True)
    coinid = Column(INTEGER(11), nullable=False)
    mintmark = Column(Enum('P', 'D', 'S'), nullable=False)
    coincondition = Column(CHAR(5), nullable=False)
    obversepic = Column(LONGBLOB)
    reversepic = Column(LONGBLOB)
    year = Column(TINYINT(4), nullable=False)
    slabbarcode = Column(String(25))
    notes = Column(TEXT)
    #coinlocation = relationship('CoinLocationDefinition')
    #coinsublocation = relationship('CoinSubLocationDefinition')
    #cointype = relationship('CoinTypesDefinition')
    #user = relationship('UsersDefinition')
    transactions = relationship("TransactionsDefinition", backref='coin')
    #transactions = relationship("TransactionsDefinition", back_populates='coins')
