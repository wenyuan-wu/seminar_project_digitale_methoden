#!/bin/bash

# get files prepared
mkdir -p marian_preprocessed
python histnorm/scripts/convert_to_charseq.py data/period_7_{train,test,dev}.tsv --to marian_preprocessed


python histnorm/scripts/evaluate.py data/period_7_dev.tsv marian_files/pred/period_7_dev_predictions.txt
