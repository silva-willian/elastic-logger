## Elastic Logger 
Solution created for segregation of logs for the elasticsearch in python

## Setup environment
```
1. If Python 3 is not installed, download it https://www.python.org/downloads/
2. If Docker is not installed, download it https://docs.docker.com/engine/installation/
3. If Docker Compose is not installed, download it https://docs.docker.com/compose/install/
4. Access the physical folder of the docker in the ./devops/docker project.
5. Run the 'docker-compose up' command at the command prompt
6. Access the url http://localhost:9200/ to access the elasticsearch
7. Access the url http://localhost:5601/ to access the Kibana
8. Run the 'python3.6 setup.py install' command at the command prompt
9. Run the 'python3.6 -m unittest tests.testLogger' command at the command prompt
10. Access the kibana to view the logs

```

## Example to use
```

from logger import Logger

logger = Logger()

list = ["a", "b"]

logger.debug("Simple debug message")

logger.debug("Degug Message with Object", list)

logger.info("Simple info message")
logger.info("Info Message with Object", list)

logger.warning("Simple warning message")
logger.warning("Warning Message with Object", list)

logger.error("Simple error message")
logger.error("Error Message with Object", list)

logger.critical("Simple critical message")
logger.critical("Critical Message with Object", list)
```

## Output
```
2018-06-11 16:13:32,357 - DEBUG - 137480372123447480 - Simple debug message
2018-06-11 16:13:32,410 - DEBUG - 137480372123447480 - Degug Message with Object - args:[ {"py/tuple": [["a", "b"]]} ]
2018-06-11 16:13:32,432 - INFO - 137480372123447480 - Simple info message
2018-06-11 16:13:32,448 - INFO - 137480372123447480 - Info Message with Object - args:[ {"py/tuple": [["a", "b"]]} ]
2018-06-11 16:13:32,465 - WARNING - 137480372123447480 - Simple warning message
2018-06-11 16:13:32,480 - WARNING - 137480372123447480 - Warning Message with Object - args:[ {"py/tuple": [["a", "b"]]} ]
2018-06-11 16:13:32,491 - ERROR - 137480372123447480 - Simple error message
2018-06-11 16:13:32,500 - ERROR - 137480372123447480 - Error Message with Object - args:[ {"py/tuple": [["a", "b"]]} ]
2018-06-11 16:13:32,514 - CRITICAL - 137480372123447480 - Simple critical message
2018-06-11 16:13:32,529 - CRITICAL - 137480372123447480 - Critical Message with Object - args:[ {"py/tuple": [["a", "b"]]} ]
```

## Configuring the environment variables
```
# configure the elasticsearch host through the elastic_logger_host environment variable
elkHost="http://localhost:9200"

# configure the index name in elasticsearch through the environment variable elastic_logger_index_name
ELASTIC-LOGGER-INDEX-NAME=elastic-logger

# configuring whether elasticsearch authentication is active
elkAuthEnable=True

# configuring ElasticSearch Authentication User
elkAuthUser=you_user

# configuring ElasticSearch Authentication Password
elkAuthPassword=your_pass

# Default values of variables
elkHost="https://localhost:9200"
ELASTIC-LOGGER-INDEX-NAME=monitor-zabbix-hosts-local
elkAuthEnable=False
elkAuthUser=
elkAuthPassword=


NOTE: Under development use python-dotenv .env file
```