#!/usr/bin/env bash

RAW=/world/data-gpu-94/sysu-reid/person-reid-data/Market-1501/
#RAW=/home/jiaojiening/data
EXP=/home/jiaojiening/data

cd $(dirname ${BASH_SOURCE[0]})/../

d=Market-1501-v15.09.15
echo "Making $d"
#python tools/make_lists_id_market.py $EXP/datasets/$d $EXP/lists/$d --val-ratio=0
python tools/make_lists_id_market.py $RAW/$d $EXP/lists/$d --val-ratio=0
