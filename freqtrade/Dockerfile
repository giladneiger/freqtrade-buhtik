FROM python:3.8.3-slim-buster
ARG BINANCE_API_KEY
ARG BINANCE_API_SECRET_KEY
ARG FREQ_API_PWD
RUN apt-get update \
    && apt-get -y install curl build-essential libssl-dev \
    && apt-get clean \
    && pip install --upgrade pip

# Prepare environment
RUN mkdir /freqtrade
WORKDIR /freqtrade

# Install TA-lib
COPY build_helpers/* /tmp/
RUN cd /tmp && /tmp/install_ta-lib.sh && rm -r /tmp/*ta-lib*

ENV LD_LIBRARY_PATH /usr/local/lib

# Install dependencies
COPY requirements.txt requirements-common.txt requirements-hyperopt.txt /freqtrade/
RUN pip install numpy --no-cache-dir \
  && pip install -r requirements-hyperopt.txt --no-cache-dir

# Install and execute
COPY . /freqtrade/
RUN pip install -e . --no-cache-dir
COPY config.json /tmp/
RUN sed -i "s|BINANCE_API_KEY|${BINANCE_API_KEY}|g" /tmp/config.json
RUN sed -i "s|BINANCE_API_SECRET_KEY|${BINANCE_API_SECRET_KEY}|g" /tmp/config.json
RUN sed -i "s|FREQ_API_PWD|${FREQ_API_PWD}|g" /tmp/config.json
ENTRYPOINT ["freqtrade"]
# Default to trade mode
CMD [ "trade" ]