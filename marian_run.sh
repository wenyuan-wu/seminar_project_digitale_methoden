#!/bin/bash

# get files prepared
mkdir -p marian_preprocessed
python histnorm/scripts/convert_to_charseq.py data/breton_{train,test,dev}.tsv --to marian_preprocessed


python histnorm/scripts/evaluate.py data/breton_dev.tsv marian_files/pred/breton_dev_predictions.txt
