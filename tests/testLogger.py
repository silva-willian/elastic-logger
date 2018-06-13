import unittest
import uuid
from elasticlogger.logger import Logger
import os
from dotenv import load_dotenv
from datetime import datetime
from elasticsearch import Elasticsearch
import time

load_dotenv(verbose=False)


class TestLogger(unittest.TestCase):
    index_name = os.getenv("elastic_logger_index_name")

    if (not index_name):
        index_name = "elastic-logger"

    index_name_day = index_name + '-' + '{0:%Y-%m-%d}'.format(datetime.now())
    elastic_logger_host = os.getenv("elastic_logger_host")
    elastic_logger_auth_enable = bool(os.getenv("elastic_logger_auth_enable"))
    elastic_logger_auth_user = os.getenv("elastic_logger_auth_user")
    elastic_logger_auth_password = os.getenv("elastic_logger_auth_password")

    if (not elastic_logger_host):
        elastic_logger_host = ["http://localhost:9200"]
    else:
        elastic_logger_host = str(elastic_logger_host).split(",")

    if (not elastic_logger_auth_enable):
        elastic_logger_auth_enable = False

    list = ["a", "b"]

    def generate_guid(self):
        return str(uuid.uuid1().time)

    def get_logger(self, id):
        es = Elasticsearch(self.elastic_logger_host)

        if (self.elastic_logger_auth_enable and self.elastic_logger_auth_user and self.elastic_logger_auth_password):
            es = Elasticsearch(self.elastic_logger_host,
                               auth=(self.elastic_logger_auth_user, self.elastic_logger_auth_password))
        else:
            es = Elasticsearch(self.elastic_logger_host)

        body = {
            'query': {
                'match': {
                    'requestId': id
                }
            }}
        return es.search(index=self.index_name_day, doc_type="logs", body=body)

    def test_logger(self):
        self.guid = self.generate_guid()
        id = self.guid
        logger = Logger(id)
        logger.debug("Simple debug message")
        logger.debug("Degug Message with Object", self.list)
        logger.info("Simple info message")
        logger.info("Info Message with Object", list)
        logger.warning("Simple warning message")
        logger.warning("Warning Message with Object", list)
        logger.error("Simple error message")
        logger.error("Error Message with Object", list)
        logger.critical("Simple criticasl message")
        logger.critical("Critical Message with Object", list)

        time.sleep(15)
        value = self.get_logger(id)
        self.assertIsNotNone(value)
        self.assertIsNotNone(value["hits"])
        self.assertIsNotNone(value["hits"]["total"])
        self.assertEqual(int(value["hits"]["total"]), 10)


if __name__ == '__main__':
    unittest.main()
