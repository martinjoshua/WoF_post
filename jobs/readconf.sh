#!/bin/bash

config() {
    python3 -c "import yaml;print(yaml.safe_load(open('$1'))$2)"
}

confl="../conf/realtime.yaml"

value1=$(config $confl "['scriptdir']")
value2=$(config $confl "['fcstroot']")
value3=$(config $confl "['starttimes']")
value4=$(config $confl "['realtime']")
value5=$(config $confl "['fields']")

echo "$value1"
echo "$value2"
echo "$value3"
echo "$value4"
echo "$value5"