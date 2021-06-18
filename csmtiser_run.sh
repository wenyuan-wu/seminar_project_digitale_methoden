#!/bin/bash

# get files prepared
mkdir -p csmtiser_preprocessed
bash histnorm/scripts/convert_to_orignorm.sh data/breton_{train,test,dev}.tsv --to csmtiser_preprocessed

docker run -v $(pwd)/csmtiser:/csmtiser greegorey/csmtiser python preprocess.py csmtiser-config.yml

docker run -v $(pwd)/csmtiser:/csmtiser greegorey/csmtiser python train.py csmtiser-config.yml

docker run -v $(pwd)/csmtiser:/csmtiser greegorey/csmtiser python normalise.py csmtiser-config.yml csmtiser_preprocessed/test.orig

python histnorm/scripts/evaluate.py data/breton_dev.tsv csmtiser/csmtiser_preprocessed/test.orig.norm
