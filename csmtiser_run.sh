#!/bin/bash

# get files prepared
mkdir -p csmtiser_preprocessed
bash histnorm/scripts/convert_to_orignorm.sh data/period_7_{train,test,dev}.tsv --to csmtiser_preprocessed

python histnorm/scripts/evaluate.py data/period_7_dev.tsv marian_files/pred/period_7_dev_predictions.txt


docker run -v $(pwd):/home greegorey/csmtiser python preprocess.py


docker run -v $(pwd)/csmtiser:/csmtiser greegorey/csmtiser python preprocess.py /csmtiser/myconfig.yml

docker run -v $(pwd)/csmtiser:/csmtiser greegorey/csmtiser python train.py /csmtiser/myconfig.yml

docker run -v $(pwd)/csmtiser:/csmtiser greegorey/csmtiser python normalise.py csmtiser-config.yaml preprocessed/test.orig
