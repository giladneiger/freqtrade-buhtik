#!/bin/bash
python3 rest_client.py balance |sed "s/'/\"/g" | jq .currencies[].balance 