import os,time,json,logging,subprocess
import logging.config
from datetime import datetime
from pythonjsonlogger import jsonlogger

def sendLogsToElasticSearch(data):
    logging.config.fileConfig('/data_handler/logging.conf')
    logger = logging.getLogger("MainLogger")
    logging.info(data)

class ElkJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(ElkJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['@timestamp'] = datetime.now().isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
time.sleep(10)
while True:
    balance = subprocess.check_output(["/bin/bash", "data_handler.sh"]).decode("utf-8").strip()
    sendLogsToElasticSearch(balance)
    time.sleep(60)


