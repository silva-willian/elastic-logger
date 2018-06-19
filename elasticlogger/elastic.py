from datetime import datetime

import jsonpickle
from elasticsearch import Elasticsearch
import threading
import os
from dotenv import load_dotenv

load_dotenv(verbose=False)


class Elastic():
    elastic_logger_host = os.getenv("elastic_logger_host")
    elastic_logger_auth_enable = bool(os.getenv("elastic_logger_auth_enable"))
    elastic_logger_auth_user = os.getenv("elastic_logger_auth_user")
    elastic_logger_auth_password = os.getenv("elastic_logger_auth_password")

    def __init__(self, _id, _index_name, _index_name_day):
        self.index_name = _index_name
        self.index_name_day = _index_name_day
        self.id = _id

        if (not self.elastic_logger_host):
            self.elastic_logger_host = ["http://localhost:9200"]
        else:
            self.elastic_logger_host = str(self.elastic_logger_host).split(",")

        if (not self.elastic_logger_auth_enable):
            self.elastic_logger_auth_enable = False

        if (self.elastic_logger_auth_enable and self.elastic_logger_auth_user and self.elastic_logger_auth_password):
            self.es = Elasticsearch(self.elastic_logger_host,
                                    auth=(self.elastic_logger_auth_user, self.elastic_logger_auth_password))
        else:
            self.es = Elasticsearch(self.elastic_logger_host)

    def post(self, severity, message, args):
        try:
            body = {"requestId": self.id, "message": message, "@timestamp": datetime.now(),
                    "application": self.index_name}

            if (severity):
                body["severity"] = str(severity)

            if (args):
                body["args"] = args

            self.es.index(index=self.index_name_day, doc_type="logs", body=body)
        except Exception as e:
            print("Elasticsearch unavaliable")
            print("An exception occurred [" + jsonpickle.encode(e) + " ]")
            pass

    def asyncPost(self, severity, message, args):
        threading.Thread(target=self.post, args=(severity, message, args)).start()
