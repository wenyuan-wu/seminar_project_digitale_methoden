# Seminarprojekt Digitale Methoden
Dieses Repository enthält die in der Seminarprojekt verwendeten Quellcodes.

## Data
- a sufficient amount of tokenized text in the historical language of your choice
- collect a list of pairs of modern and historical words (e.g. a couple of hundreds to a thousand) 
  and try various normalization models on them
  
## Approaches
5 approaches tested

### Norma
Norma is a tool for automatic spelling normalization of non-standard language data. It uses a combination of different 
normalization techniques that typically require training data (= a list of manually normalized wordforms) 
and a target dictionary (= a list of valid wordforms in the target language).

[GitHub](https://github.com/comphist/norma)

- At the moment, normalizers are restricted to work with one word at a time. 
  That means they cannot take context into account or contract several words into one. 
  We're planning to build further functionality on top of the existing normalizers to enable this.

#### Environment setup

[GFSM finite state machine library](http://kaskade.dwds.de/~moocow/mirror/projects/gfsm/)
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

```commandline
docker run -v $(pwd):/home mbollmann/norma
docker run -v $(pwd):/home mbollmann/norma -s -c doc/example/example.cfg -f doc/example/fnhd_sample.txt
```

## Resources
- [Historical Text Normalization](https://github.com/coastalcph/histnorm#tldr-the-recommended-normalization-approach)
- [Neural transducer baseline](https://github.com/peter-makarov/il-reimplementation/tree/feature/sgm2021)

