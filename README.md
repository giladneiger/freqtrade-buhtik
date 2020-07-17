# freqtrade-buhtik
This repository is a DevOps upgraded version for the successful freqtrade bot. Including data collection & visualization, using Elasticsearch, logstash & Kibana

## Prerequisites
In order to run the freqtrade-buhtik, you'll have to have these requirements installed:
* Docker
* Docker-compose

## Diff
What are the changes from the normal Freqtrade project?
We've added:
* Data handler container (written in Python) - getting relevant data from the freqtrade API and saves it in a log file. Information regarding the data is detailed below
* A data collector & analyze - Logstash & Elasticsearch in 2 different containers
* Visualization - using Kibana, you can take all that data and make dashboards from them

## Data
The data collected from the freqtrade API and delivered to Elasticsearch & Kibana includes:
* Current BTC in account
* Current value in dollars
* Current best pair of trading
* Average duration for trades
* Latest trade done (date)
* Total trades done
* Current open trades 

## Credentials
In order to allow full control for the bot & the ELK (Elasticsearch, Logstash, Kibana) services,you should inject the credentials to the containers. The best way to do so is to create a credentials file called .env (include it in .gitignore) so git won't save it. Set the following environment variables inside this file:

* BINANCE_API_KEY
* BINANCE_API_SECRET_KEY
* FREQ_API_PWD
* ELASTIC_PASSWORD
* TELEGRAM_TOKEN
* TELEGRAM_CHAT_ID

The user for logging in to the Kibana GUI: elastic

## Default configuration
These are the default configurations I put for the trading freqtrade bot, you can change it on the config.json:
* stake_currency: BTC
* stake_amount: unlimited
* tradable_balance_ratio: 1

## Coins trade list
The coins pairs that are allowed to be trade by freqtrade are:
* EOS/BTC
* ETH/BTC
* LINK/BTC
* NEO/BTC
* XRP/BTC
* XTZ/BTC
* MATIC/BTC
* VET/BTC
* ADA/BTC
* BAND/BTC
* DOGE/BTC
* XLM/BTC
* ATOM/BTC
* LEND/BTC
* ERD/BTC
* ZIL/BTC
* ONT/BTC
* ANKR/BTC
* SOL/BTC
* COMP/BTC
* STORJ/BTC
* KAVA/BTC


## How to run the freqtrade-buhtik
Firstly, build the docker images locally by:
```
docker-compose build
```
Secondly, run the docker-compose:
```
docker-compose up
```






