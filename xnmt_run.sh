#!/bin/bash

# get files prepared
mkdir -p marian_preprocessed
python histnorm/scripts/convert_to_charseq.py data/period_7_{train,test,dev}.tsv --to marian_preprocessed


python histnorm/scripts/evaluate.py data/period_7_dev.tsv marian_files/pred/period_7_dev_predictions.txt

PYTHONHASHSEED=0 python3 -m xnmt.xnmt_run_experiments xnmt-config.yaml --dynet-seed 0 --dynet--gpu
