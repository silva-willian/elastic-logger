from datetime import datetime
import logging
import uuid
from elasticlogger.elastic import Elastic
import os
from dotenv import load_dotenv
import jsonpickle

load_dotenv(verbose=False)


class Logger():

    def __init__(self, _id=None):

        if (not _id):
            self.generateId()
        else:
            self.id = str(_id)

        self.base_init()

    def base_init(self):
        index_name = os.getenv("elastic_logger_index_name")

        if (not index_name):
            index_name = "elastic-logger"

        index_name_day = index_name + '-' + '{0:%Y-%m-%d}'.format(datetime.now())

        log = logging.getLogger(index_name_day)
        log.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.NOTSET)

        # create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        log.addHandler(ch)

        self.elastic = Elastic(self.id, index_name, index_name_day)
        self.log = log

    def generateId(self):
        self.id = str(uuid.uuid1().time)

    def info(self, message, *args):
        self.logger(logging.INFO, message, args)

    def debug(self, message, *args):
        self.logger(logging.DEBUG, message, args)

    def warning(self, message, *args):
        self.logger(logging.WARNING, message, args)

    def critical(self, message, *args):
        self.logger(logging.CRITICAL, message, args)

    def error(self, message, *args):
        self.logger(logging.ERROR, message, args)

    def logger(self, level, message, args=""):
        args_message = ''

        if (args):
            args = jsonpickle.encode(args)
            args_message = " - args:[ " + args + " ]"

        self.log.log(level, self.id + ' - ' + message + args_message)
        self.elastic.asyncPost(logging.getLevelName(level), message, args)
