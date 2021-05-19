#!/bin/bash

docker run -v $(pwd):/home --entrypoint norma_lexicon mbollmann/norma -w data/period_7_words.txt -a norma_files/period_7.fsm -l norma_files/period_7.sym -c
docker run -v $(pwd):/home mbollmann/norma -c norma_files/norma.cfg -f data/period_7_train.csv -s -t --saveonexit
docker run -v $(pwd):/home mbollmann/norma -c norma_files/norma.cfg -f data/period_7_test_singcol.txt -s > norma_files/period_7_predictions.csv
