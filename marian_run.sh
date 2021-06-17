#!/bin/bash

# get files prepared
mkdir -p csmt_preprocessed
python histnorm/scripts/convert_to_charseq.py data/period_7_{train,test,dev}.tsv --to csmt_preprocessed


python histnorm/scripts/evaluate.py data/period_7_dev.tsv csmt_files/pred/period_7_dev_predictions.txt
