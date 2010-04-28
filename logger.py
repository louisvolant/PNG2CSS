#!/usr/bin/env python
#

"""General logging interface for the application."""

import logging
import logging.handlers
import settings


class Logger():
    """Provides a general logging interface for the application."""
    __instance = None


    class FileLogger():
        """Provides an interface to log in files."""
        log = None

        def __init__(self):
            """ Logger's initialisation based on settings parameters. """
            self.log = logging.getLogger(settings.APPLICATION_NAME)
            logging.NOLOG = 60
            logging.addLevelName(logging.NOLOG, 'NOLOG')
            #SYSLOG LEVEL
            if settings.LOG_LEVEL == 'CRITICAL':
                self.log.setLevel(logging.CRITICAL)
            elif settings.LOG_LEVEL == 'ERROR':
                self.log.setLevel(logging.ERROR)
            elif settings.LOG_LEVEL == 'WARNING':
                self.log.setLevel(logging.WARNING)
            elif settings.LOG_LEVEL == 'INFO':
                self.log.setLevel(logging.INFO)
            elif settings.LOG_LEVEL == 'DEBUG':
                self.log.setLevel(logging.DEBUG)
            else:
                #Superior than CRITICAL
                self.log.setLevel(logging.NOLOG)

            #File handler
            filelog = logging.handlers.RotatingFileHandler(
                        settings.LOG_FILENAME,
                        maxBytes=settings.LOG_FILESIZE,
                        backupCount=settings.LOG_NBLOGFILES
                      )

            #Formatter
            if len(settings.LOG_FORMATTER) == 0:
                formatter = logging._defaultFormatter
            else:
                formatter = logging.Formatter(settings.LOG_FORMATTER)

            filelog.setFormatter(formatter)
            self.log.addHandler(filelog)


    def __init__(self):
        """Create instance of Syslog logger if doesn't exists."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()

    def warn(self,message):
        """Produce log message with WARNING level."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()
        Logger.__instance.log.warn(message)

    def debug(self,message):
        """Produce log message with DEBUG level."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()
        Logger.__instance.log.debug(message)

    def info(self,message):
        """Produce log message with INFO level."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()
        Logger.__instance.log.info(message)

    def error(self,message):
        """Produce log message with ERROR level."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()
        Logger.__instance.log.error(message)

    def critical(self,message):
        """Produce log message with CRITICAL level."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()
        Logger.__instance.log.critical(message)

    def __new__(Logger):
        """Create and return instance of Syslog logger if doesn't exists."""
        if not Logger.__instance :
            Logger.__instance = Logger.FileLogger()
        return Logger.__instance


logger = Logger()


def warn(message):
    """Produce log message with WARNING level."""
    logger.warn(message)


def debug(message):
    """Produce log message with DEBUG level."""
    logger.debug(message)


def info(message):
    """Produce log message with INFO level."""
    logger.info(message)


def error(message):
    """Produce log message with ERROR level."""
    logger.error(message)


def critical(message):
    """Produce log message with CRITICAL level."""
    logger.critical(message)