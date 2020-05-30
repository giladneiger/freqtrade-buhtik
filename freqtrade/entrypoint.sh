#!/bin/bash
sed -i "s|BINANCE_API_KEY|${BINANCE_API_KEY}|g" /tmp/config.json
sed -i "s|BINANCE_API_SECRET_KEY|${BINANCE_API_SECRET_KEY}|g" /tmp/config.json