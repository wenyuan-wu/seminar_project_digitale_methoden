#!/bin/bash

MODEL_DIR=marian_files
mkdir -p ${MODEL_DIR}/pred

MARIAN_PATH=marian/build
WORKSPACE=3500 #change this value to fit your GPU memory

cat marian_preprocessed/dev.src | $MARIAN_PATH/marian-decoder \
    -c $MODEL_DIR/model.npz.best-perplexity.npz.decoder.yml \
    -m $MODEL_DIR/model.npz.best-perplexity.npz --quiet-translation \
    --devices 0 --mini-batch 16 --maxi-batch 100 --maxi-batch-sort src \
    -w $WORKSPACE --beam-size 5 | sed 's/ //g' > ${MODEL_DIR}/pred/period_7_dev_predictions.txt
