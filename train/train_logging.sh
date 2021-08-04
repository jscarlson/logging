#!/bin/bash

while IFS= read -r line
do
    echo "$line"
    python ./logging/train/train_logging.py "$1" "$line"
done
