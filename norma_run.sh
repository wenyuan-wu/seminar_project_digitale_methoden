#!/bin/bash

# proper permission for docker
sudo chmod 666 /var/run/docker.sock

# get files prepared
cut -f2 data/breton_raw.tsv > data/breton_words.txt
cut -f1 data/breton_dev.tsv > data/breton_dev_singcol.txt

# training norma and perform prediction
start="date +%s"

mkdir -p norma_files

docker run -v $(pwd):/home --entrypoint norma_lexicon mbollmann/norma -w data/breton_words.txt -a norma_files/breton.fsm -l norma_files/breton.sym -c
docker run -v $(pwd):/home mbollmann/norma -c norma_files/norma.cfg -f data/breton_train.tsv -s -t --saveonexit
docker run -v $(pwd):/home mbollmann/norma -c norma_files/norma.cfg -f data/breton_dev_singcol.txt -s > norma_files/breton_predictions.tsv

# measure time spent
end="date +%s.%N"
runtime=$((end-start))
echo "runtime: $runtime seconds"

# better result inspection
paste -d "\t" data/breton_dev.tsv norma_files/breton_predictions.tsv > norma_files/breton_dev_results.tsv
