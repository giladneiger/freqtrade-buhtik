#!/bin/bash
python3 rest_client.py profit | sed "s/'/\"/g" | jq '.trade_count'