from sqlalchemy.testing import in_

from DatabaseComponents import DatabaseComponents
from Logger import Logger
from databasedefinitions.DatabaseDefinitions import *

class MenuDatabase:

    def __init__(self, databasecomponent: DatabaseComponents, log: Logger):
            self.database = databasecomponent
            self.logger = log.genereatelogger(__name__)


    def getcoinlocation(self, sessionid: str):

        try:
            session = self.database.genereateSession()
            subquery = session.query(UsersDefinition.userid).join(SessionsDefinition).filter(
            SessionsDefinition.sessionguid == sessionid).subquery()
            result = session.query(CoinLocationDefinition.locationid, CoinLocationDefinition.location).join(UsersDefinition).filter(UsersDefinition.userid.in_(subquery)).all()
            resultset = []
            for row in result:
                location = CoinLocationDefinition()
                location.locationid = row.locationid
                location.location = row.location
                resultset.append(location)
            return resultset
        finally:
            self.database.closeSession()

    def getsublocations(self, locationid: int):

        try:
            session = self.database.genereateSession()
            result = session.query(CoinSubLocationDefinition.sublocationid, CoinSubLocationDefinition.sublocation).filter(CoinSubLocationDefinition.locationfk == locationid).all()
            resultset = []
            for row in result:
                coinlocation = CoinSubLocationDefinition()
                coinlocation.sublocationid = row.sublocationid
                coinlocation.sublocation = row.sublocation
                resultset.append(coinlocation)
            return resultset
        finally:
            self.database.closeSession()

    def getcointypes(self, sessionid: str):
        try:
            session = self.database.genereateSession()
            subquery = session.query(UsersDefinition.userid).join(SessionsDefinition).filter(
                SessionsDefinition.sessionguid == sessionid).subquery()
            result = session.query(CoinTypesDefinition.typeid, CoinTypesDefinition.type).join(UsersDefinition).filter(UsersDefinition.userid.in_(subquery)).all()
            resultset = []
            for row in result:
                ct = CoinTypesDefinition()
                ct.typeid = row.typeid
                ct.type = row.type
                resultset.append(ct)
            return resultset
        finally:
            self.database.closeSession()

    def getsources(self, sessionid: str):
        try:
            session = self.database.genereateSession()
            subquery = session.query(UsersDefinition.userid).join(SessionsDefinition).filter(
                SessionsDefinition.sessionguid == sessionid).subquery()
            result = session.query(SourceDefinition.sourceid, SourceDefinition.source).join(UsersDefinition).filter(UsersDefinition.userid.in_(subquery)).all()
            resultset = []
            for row in result:
                source = SourceDefinition()
                source.sourceid = row.sourceid
                source.source = row.source
                resultset.append(source)
            return resultset
        finally:
            self.database.closeSession()

if __name__ == '__main__':
    log = Logger()
    dbc = DatabaseComponents(log)

    menu = MenuDatabase(dbc, log)
    data = menu.getcointypes("205de6bd-bfb3-4953-b8c1-2fe3200fefd6")
    print(len(data))
    print(data[0].type)
