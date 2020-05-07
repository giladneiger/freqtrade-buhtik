#!/bin/bash
python3 rest_client.py status | sed "s/'/\"/g" | jq .[] 