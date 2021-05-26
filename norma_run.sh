#!/bin/bash

# proper permission for docker
sudo chmod 666 /var/run/docker.sock

# get files prepared
cut -f2 data/period_7_raw.tsv > data/period_7_words.txt
cut -f1 data/period_7_dev.tsv > data/period_7_dev_singcol.txt

# training norma and perform prediction
start="date +%s"

docker run -v $(pwd):/home --entrypoint norma_lexicon mbollmann/norma -w data/period_7_words.txt -a norma_files/period_7.fsm -l norma_files/period_7.sym -c
docker run -v $(pwd):/home mbollmann/norma -c norma_files/norma.cfg -f data/period_7_train.tsv -s -t --saveonexit
docker run -v $(pwd):/home mbollmann/norma -c norma_files/norma.cfg -f data/period_7_dev_singcol.txt -s > norma_files/period_7_predictions.tsv

# measure time spent
end="date +%s.%N"
runtime=$((end-start))
echo "runtime: $runtime seconds"

# better result inspection
paste -d "\t" data/period_7_dev.tsv norma_files/period_7_predictions.tsv > norma_files/period_7_dev_results.tsv
