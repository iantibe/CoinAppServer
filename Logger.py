import logging

from Constants import Constants


class Logger:
    def __init__(self):
        pass

    def genereatelogger(self, modulename):
        logging.basicConfig(level=logging.INFO, filename=Constants.LOGGERNAME, format='%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
        logger = logging.getLogger(modulename)
        return logger
