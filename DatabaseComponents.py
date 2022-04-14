from Constants import Constants
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
from Logger import Logger


class DatabaseComponents:
    def __init__(self, logger: Logger):
        self.objectsession = None
        self.engine = None
        self.loggerobject = logger.genereatelogger(__name__)


    def genereateSession(self):
        try:
            self.engine = create_engine(Constants.DATABASEURL, pool_pre_ping=True)
            session = sessionmaker(bind=self.engine)
            self.objectsession = session()
            return self.objectsession
        except:
            self.loggerobject.exception("An excpetion occured in method generateSession")


    def closeSession(self):
        self.objectsession.close()
        self.engine.dispose()

