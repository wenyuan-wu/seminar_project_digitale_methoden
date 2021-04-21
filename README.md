# Seminarprojekt Digitale Methoden
Dieses Repository enthält die in der Seminarprojekt verwendeten Quellcodes.

## Data
- a sufficient amount of tokenized text in the historical language of your choice
- collect a list of pairs of modern and historical words (e.g. a couple of hundreds to a thousand) 
  and try various normalization models on them
  
## Approaches
### Norma
Norma is a tool for automatic spelling normalization of non-standard language data. It uses a combination of different 
normalization techniques that typically require training data (= a list of manually normalized wordforms) 
and a target dictionary (= a list of valid wordforms in the target language).

[GitHub](https://github.com/comphist/norma)

- At the moment, normalizers are restricted to work with one word at a time. 
  That means they cannot take context into account or contract several words into one. 
  We're planning to build further functionality on top of the existing normalizers to enable this.



## Resources
- [Historical Text Normalization](https://github.com/coastalcph/histnorm#tldr-the-recommended-normalization-approach)
- [Neural transducer baseline](https://github.com/peter-makarov/il-reimplementation/tree/feature/sgm2021)