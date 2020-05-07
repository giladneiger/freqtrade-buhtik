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
        log_record['open_trades'] = open_trades
        log_record['total_trades_done'] = total_trades_done
time.sleep(10)
while True:
    balance = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/balance.sh"]).decode("utf-8").strip()
    open_trades = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/open_trades.sh"]).decode("utf-8").strip()
    if open_trades == None or open_trades == "":
        open_trades = 0
    total_trades_done = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/total_trades_done.sh"]).decode("utf-8").strip()
    sendLogsToElasticSearch(balance)
    time.sleep(1800)


