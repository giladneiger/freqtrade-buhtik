#!/bin/bash
python3 rest_client.py count | sed "s/'/\"/g" | jq '.current'