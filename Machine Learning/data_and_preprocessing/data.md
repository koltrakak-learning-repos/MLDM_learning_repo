# What is a data set?

Narrow view

- a set of N individuals
- each individual is described by D values
- in essence it could be seen as a relational table with N rows and D columns

Broader view

- all other kinds of data that can't be described as above (semi-structured, unstructured)
- in most of the cases data are not so nicely arranged
- many machine learning techniques require that the dataset is provided as a relational table
  - **we need to apply transformations**
  - preprocessing gives us this nice table

# Types of data

descriptive statistics = measures that describe status of something -> stuff like mean, median, variance, ...

1. Categorical: simboli
    - nominal
        - The values are a set of labels
        - the available information allows to distinguish a label from another
    - ordinal
        - come sopra ma c'è una relazione di ordinamento
        - bad, medium, good

2. Numerical: numeri
    - interval
        - the difference is meaningful (possiamo misurare distanze e definire intervalli) but they don't have a univocal zero
        - temperatures
            - Zero is an arbitrary value, hence, 0°C and 0°F indicate different temperatures.
            - Given two temperatures t1=10°C and t2=12°C it does not have any sense to say that their relative difference is 20%, **changing the scale the relative difference would change**
    - ratio
        - hanno uno zero univoco, ha quindi senso misurare dei ratio
        - lunghezze, masse

interval data are numbers, but not quite. They miss a unique zero

ratio data have a meaningful answer to questions like is a twice as much as b?

nominals and ordinals are discrete

intervals and ratio are continuous

### General characteristics of data sets

Un attributo asimmetrico è un tipo di attributo binario (cioè con due valori: 0/1, vero/falso, sì/no) in cui solo la presenza (1) è considerata informativa, mentre l’assenza (0) non è interessante.

- e.g esame passato -> asimmetrico; sesso: m/f -> simmetrico

...

# Data Quality

data can have some issues, particularly when integrating from different sources (pensa a duplication e inconsistencies)

- Noise, missing, inconsistent, duplicated, wrong
- Outliers, small amount of data which are different from the rest due to anomalies, noise or errors

Data preprocessing can augment the quality of data

outliers can be generated from a rare event or from noise... it's not easy to distinguish between the two cases

## Management of missing values

- do not consider objects with missing values (sometimes not a good idea)
- estimate/default

interessante il fatto che un dato null possa significare due cose:

- non so la targa della macchina
- so che la targa non esiste

## Detecting outliers tramite inter-quartile-range

Questa tecnica si basa sulla suddivisione dei dati in quartili:

- Q1 (primo quartile): il 25% dei dati è sotto questo valore
- Q2 (mediana): il 50% dei dati è sotto questo valore
- Q3 (terzo quartile): il 75% dei dati è sotto questo valore

L’IQR (InterQuartile Range) rappresenta l’ampiezza della parte centrale dei dati: IQR=Q3−Q1

- **Misura la dispersione dei dati senza farsi influenzare dagli outlier.**
- L’idea è che i valori troppo lontani dal “cuore” della distribuzione siano probabilmente outlier.

Si definiscono due limiti (boundary):

- Lower Boundary: Q1 − 1.5*IQR
- Upper Boundary: Q3 + 1.5*IQR

Un valore è considerato outlier se è più piccolo del limite inferiore, oppure è più grande del limite superiore

Nei boxplot:

- la scatola va da Q1 a Q3
  - la linea dentro la scatola è la mediana (Q2)
- i whisker (baffi) arrivano fino all’ultimo valore dentro i boundary
  - per questo non sono simmetrici
- i valori fuori dai baffi sono segnati come outlier (puntini)
