import abc
import datetime
from Logger import Logger
from Constants import Constants
from DatabaseLogon import DatabaseLogon
from exceptions.MultipleSessionsFound import MultipleSessionsFound


class APIBase(metaclass=abc.ABCMeta):

    def __init__(self, database: DatabaseLogon, log: Logger):
        #TODO move input database classes to thier own class, out of databaselogon
        self.database = database
        self.logobject = log.genereatelogger(__name__)

    def validatelogonsession(self, session: str) -> bool:
        if session == Constants.AUTHENTICATIONHEADERFORLOGON:
            return True
        else:
            return False

    @abc.abstractmethod
    def activate(self, json: str, authkey: str):
        pass

    def _checksessionexist(self, session: str):

        data = self.database.queryopensessionexist(session)
        if len(data) == 0:
            return False
        if len(data) > 1:
            raise MultipleSessionsFound("Multiple sessions found")
        #TODO if multiple sessions found, log them all out
        for row in data:
            if (row["start"] + datetime.timedelta(days=Constants.PASSWORDLIFETIME)) > datetime.datetime.now():
                return True
            else:
                self.database.insertLogout(session)
                self.logobject.info("Session: "+ session + "Has automatically been logged out due to an expired session")
                return False

    def validateregularsession(self, session: str):
        # TODO TEST this method

        if self._checksessionexist(session):
            self.logobject.info("Session: " + str(session) + " has been validated")
            return True

        else:
            self.logobject.info("Session: " + str(session) + " has been rejected")
            return False



