#!/bin/bash

THRESHOLD="$1"  # in percents
ENDPOINT="$2"

while true; do
    MEMORY=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    if (( $(echo "$MEMORY > $THRESHOLD" |bc -l) )); then
        curl -X POST -H "Content-Type: application/json" -d '{"message": "Memory usage exceeded the threshold of '$THRESHOLD'%"}' $ENDPOINT
        sleep 300  # 5 minutes
    fi
    sleep 10;
done
