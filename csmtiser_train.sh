#!/bin/bash

# get files prepared
mkdir -p csmtiser_preprocessed
bash histnorm/scripts/convert_to_orignorm.sh data/period_7_{train,test,dev}.tsv --to csmtiser_preprocessed

python histnorm/scripts/evaluate.py data/period_7_dev.tsv marian_files/pred/period_7_dev_predictions.txt
