from datetime import datetime

import jsonpickle
from elasticsearch import Elasticsearch
import threading
import os
from dotenv import load_dotenv

load_dotenv(verbose=False)


class Elastic():
    elastic_logger_host = os.getenv("elkHost")
    elastic_logger_port = os.getenv("elkPort")
    elastic_logger_auth_enable = bool(os.getenv("elkAuthEnable"))
    elastic_logger_auth_user = os.getenv("elkAuthUser")
    elastic_logger_auth_password = os.getenv("elkAuthPassword")

    def __init__(self, _id, _index_name, _index_name_day):
        self.index_name = _index_name
        self.index_name_day = _index_name_day
        self.id = _id

        if (not self.elastic_logger_host):
            self.elastic_logger_host = ["http://localhost"]
        else:
            self.elastic_logger_host = str(self.elastic_logger_host).split(",")

        if (not self.elastic_logger_port):
            self.elastic_logger_port = 9200

        if (not self.elastic_logger_auth_enable):
            self.elastic_logger_auth_enable = False

        if (self.elastic_logger_auth_enable and self.elastic_logger_auth_user and self.elastic_logger_auth_password):
            self.es = Elasticsearch(hosts=self.elastic_logger_host, port=self.elastic_logger_port,
                                    auth=(self.elastic_logger_auth_user, self.elastic_logger_auth_password))
        else:
            self.es = Elasticsearch(hosts=self.elastic_logger_host, port=self.elastic_logger_port)

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
