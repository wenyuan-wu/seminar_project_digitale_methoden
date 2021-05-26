#!/bin/bash

# get files prepared
cut -f1 norma_files/period_7_predictions.tsv > norma_files/period_7_predictions_singcol.tsv
python histnorm/scripts/evaluate.py data/period_7_dev.tsv norma_files/period_7_predictions_singcol.tsv
