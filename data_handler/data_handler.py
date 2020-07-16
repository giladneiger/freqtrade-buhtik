import os,time,json,logging,subprocess,requests
import logging.config
from datetime import datetime
from pythonjsonlogger import jsonlogger

def sendLogsToElasticSearch(data):
    logging.config.fileConfig('/data_handler/logging.conf')
    logger = logging.getLogger("MainLogger")
    logging.info(data)

def getBtcValue(btc_amount):
    API_ENDPOINT = "https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT"
    response = requests.get(API_ENDPOINT).json()
    btc_value = float(response['price'])
    return (btc_value * float(btc_amount))

class ElkJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(ElkJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['@timestamp'] = datetime.now().isoformat()
        log_record['level'] = record.levelname
        log_record['logger'] = record.name
        log_record['open_trades'] = open_trades
        log_record['total_trades_done'] = total_trades_done
        log_record['best_pair'] = best_pair
        log_record['latest_trade_date'] = latest_trade_date
        log_record['avg_duration'] = avg_duration
        log_record['dollars_in_account'] = dollars_in_account
time.sleep(10)
while True:
    balance = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/balance.sh"]).decode("utf-8").strip()
    open_trades = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/open_trades.sh"]).decode("utf-8").strip()
    if open_trades == None or open_trades == "":
        open_trades = 0
    total_trades_done = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/total_trades_done.sh"]).decode("utf-8").strip()
    best_pair = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/best_pair.sh"]).decode("utf-8").strip()
    latest_trade_date = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/latest_trade_date.sh"]).decode("utf-8").strip()
    avg_duration = subprocess.check_output(["/bin/bash", "/data_handler/api_commands/avg_duration.sh"]).decode("utf-8").strip()
    dollars_in_account = getBtcValue(balance)
    sendLogsToElasticSearch(balance)
    time.sleep(60)


