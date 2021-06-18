#!/bin/bash

# get files prepared
cut -f1 norma_files/breton_predictions.tsv > norma_files/breton_predictions_singcol.tsv
python histnorm/scripts/evaluate.py data/breton_dev.tsv norma_files/breton_predictions_singcol.tsv
