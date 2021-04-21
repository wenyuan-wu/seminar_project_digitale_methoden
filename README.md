# Seminarprojekt Digitale Methoden
Dieses Repository enthält die in der Seminarprojekt verwendeten Quellcodes.

## Data
- a sufficient amount of tokenized text in the historical language of your choice
- collect a list of pairs of modern and historical words (e.g. a couple of hundreds to a thousand) 
  and try various normalization models on them
  


## Approaches
5 approaches tested

### 1. Norma
[Norma](https://github.com/comphist/norma), described in [Bollmann
  (2012)](https://marcel.bollmann.me/pub/acrh12.pdf)

Norma is a tool for automatic spelling normalization of non-standard language data. It uses a combination of different 
normalization techniques that typically require training data (= a list of manually normalized wordforms) 
and a target dictionary (= a list of valid wordforms in the target language).

[GitHub](https://github.com/comphist/norma)

- At the moment, normalizers are restricted to work with one word at a time. 
  That means they cannot take context into account or contract several words into one. 
  We're planning to build further functionality on top of the existing normalizers to enable this.

#### Environment setup
Due to the lack of 
[GFSM finite state machine library](http://kaskade.dwds.de/~moocow/mirror/projects/gfsm/)
dependency on local environment approach with docker will be used.

- build from scratch
```commandline
sudo apt update
sudo apt install build-essential
sudo apt install manpages-dev
gcc --version
sudo snap install cmake --classic
cmake --version
sudo apt install libboost-all-dev
sudo apt install pkg-config
sudo apt install libglib2.0-*
sudo apt install icu-devtools
sudo apt install doxygen
```
- docker
```commandline
docker run -v $(pwd):/home mbollmann/norma
docker run -v $(pwd):/home mbollmann/norma -s -c doc/example/example.cfg -f doc/example/fnhd_sample.txt
```

### 2. Marian (NMT) for normalization
[Marian (NMT) for normalization](https://github.com/tanggongbo/normalization-NMT),
  described in [Tang et al. (2018)](http://aclweb.org/anthology/C18-1112)

### 3. XNMT

[XNMT](https://github.com/neulab/xnmt), following the model of [Bollmann
  (2018)](http://www.linguistics.rub.de/forschung/arbeitsberichte/22.pdf)

### 4. cSMTiser

[cSMTiser](https://github.com/clarinsi/csmtiser) (wrapping Moses)

### 5. Neural Transducer

[Neural Transducer](https://github.com/peter-makarov/il-reimplementation/tree/feature/sgm2021)
described in [Makarov 2020](https://www.aclweb.org/anthology/2020.acl-main.650/)

## Resources
- [Historical Text Normalization](https://github.com/coastalcph/histnorm#tldr-the-recommended-normalization-approach)
- [Neural transducer baseline](https://github.com/peter-makarov/il-reimplementation/tree/feature/sgm2021)

