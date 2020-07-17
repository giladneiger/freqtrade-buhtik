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

Credential | Detail
--- | ---
BINANCE_API_KEY | The API key of your Binance account
BINANCE_API_SECRET_KEY | The API secret key of your Binance account
FREQ_API_PWD | The freqtrade API password to use (you set it by this variable)
ELASTIC_PASSWORD | The password for your elastic user to use (login credential for Kibana)
TELEGRAM_TOKEN | The token of your telegram bot 
TELEGRAM_CHAT_ID | Your private telegram user chat ID

The user for logging in to the Kibana GUI: elastic

## Telegram bot
If you connect the freqtrade-buhtik bot to a telegram bot, it makes it easier to query infromation from the freqtrade-buhtik bot. For more informatio:
https://www.freqtrade.io/en/latest/telegram-usage/

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
Firstly set your credentials file (.env) with the required credentials mentioned above. After you set up the file, load the value to environment variables by the command:
```
source .env
```
Secondly, build the docker images locally by:
```
docker-compose build
```
Thirdly, run the docker-compose:
```
docker-compose up
```






