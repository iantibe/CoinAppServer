import datetime
import uuid

from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from Constants import Constants
from DatabaseComponents import DatabaseComponents
from Logger import Logger

from exceptions.MultipleSessionsFound import MultipleSessionsFound
from exceptions.DuplicateUserException import DuplicateUserException
from exceptions.NoPasswordBlockExistsForUser import NoPasswordBlockExistsForUser
from exceptions.NoSessionFound import NoSessionFound
from exceptions.NoUserExistsException import NoUserExistsException
from databasedefinitions.DatabaseDefinitions import UsersDefinition
from databasedefinitions.DatabaseDefinitions import SessionsDefinition

class DatabaseLogon:
    def __init__(self, databasecomponents: DatabaseComponents, log: Logger):
        self.databasecomponents = databasecomponents
        self.logobject = log.genereatelogger(__name__)

    def getPasswordBlock(self, userid):
        try:
            dbase = self.databasecomponents.genereateSession()
            result = dbase.query(UsersDefinition.password).filter(UsersDefinition.userid == userid).first()
            if result['password'] == '':
                raise NoPasswordBlockExistsForUser("No password block exists for " + userid)
            return result["password"]
        finally:
            self.databasecomponents.closeSession()

    def checkDatabaseForUserExistForLogin(self, uname: str):
        try:
            dbase = self.databasecomponents.genereateSession()
            result = dbase.query(UsersDefinition.userid).filter(UsersDefinition.username == uname).one()
            return result["userid"]
        except NoResultFound:
            raise NoUserExistsException(uname+ " " + "Does not exist")
        except MultipleResultsFound:
            raise DuplicateUserException("Duplicate user exists for " + " " + uname)
        finally:
            self.databasecomponents.closeSession()

    def checkDatabaseForExistingUserforNewUser(self, uname: str):

        try:
            dbase = self.databasecomponents.genereateSession()
            result = dbase.query(UsersDefinition.userid).filter(UsersDefinition.username == uname).all()
            return result
        finally:
            self.databasecomponents.closeSession()

    def insertNewUser(self, fname: str, lname: str, pw, uname: str):
        #TODO invetigate if we need to add an exception in this exception clause to trigger an exception in main api file
        try:
            dbase = self.databasecomponents.genereateSession()
            user = UsersDefinition(firstname=fname, lastname=lname, password=pw, username=uname)
            dbase.add(user)
            dbase.commit()
        except:
            dbase.rollback()
            self.logobject.error("Exception in insertNewUSer method of " + str(__name__))
            raise Exception("Excpetion in insertNewUser method of " + str(__name__))
        finally:
            self.databasecomponents.closeSession()

    def createSession(self, userid):
        #TODO investiage if we need to add an excpetion in this exception clause to trigger an exception in main api file
        try:
            dbase = self.databasecomponents.genereateSession()
            sessionid = uuid.uuid4()
            #todo add session using a user object
            sess = SessionsDefinition(usersfk=userid, start=datetime.datetime.now(), sessionguid=sessionid)
            dbase.add(sess)
            dbase.commit()
            return sessionid
        except:
            dbase.rollback()
            self.logobject.error("Exception in createSession method of " + str(__name__))
            raise Exception("Exception in createSession method of" + str(__name__))
        finally:
            self.databasecomponents.closeSession()

    def updatepassword(self, userid, pw):
        try:
            dbase = self.databasecomponents.genereateSession()
            query = dbase.query(UsersDefinition).filter(UsersDefinition.userid == userid).one()
            query.password = pw
            dbase.commit()
        except NoResultFound as e:
            dbase.rollback()
            raise NoUserExistsException("No user was found")
        except MultipleResultsFound as e:
            dbase.rollback()
            raise DuplicateUserException("Multiple users found")
        finally:
            self.databasecomponents.closeSession()

    def insertLogout(self, session: str):
        try:
            dbase = self.databasecomponents.genereateSession()
            query = dbase.query(SessionsDefinition).filter(and_(SessionsDefinition.sessionguid == session, SessionsDefinition.end == None)).one()
            query.end = datetime.datetime.now()
            dbase.commit()
        except NoResultFound as e:
            dbase.rollback()
            raise NoSessionFound("No Session Found in database")
        except MultipleResultsFound as e:
            dbase.rollback()
            raise MultipleSessionsFound("Multiple Sessions Found")
        finally:
            self.databasecomponents.closeSession()

    def getuserfullname(self, userid):
        try:
            dbase = self.databasecomponents.genereateSession()
            query = dbase.query(UsersDefinition.firstname, UsersDefinition.lastname).filter(UsersDefinition.userid ==userid).one()

            return query["firstname"] + " " + query["lastname"]

        except NoResultFound as e:
            raise NoUserExistsException("No user was found")
        except MultipleResultsFound as e:
            raise DuplicateUserException("Multiple users found")
        finally:
            self.databasecomponents.closeSession()

    def queryopensessionexist(self, session: str):
        #TODO Test this method
        try:
            dbase = self.databasecomponents.genereateSession()
            return dbase.query(SessionsDefinition.start).filter(and_(SessionsDefinition.sessionguid == session, SessionsDefinition.end == None)).all()
        finally:
            self.databasecomponents.closeSession()



if __name__ == '__main__':
    c = Constants()
    log = Logger(c)
    dbc = DatabaseComponents( log)
    log = Logger(c)
    data = DatabaseLogon(dbc, log)
    print(data.checkDatabaseForExistingUserforNewUser("bd67c35c"))







