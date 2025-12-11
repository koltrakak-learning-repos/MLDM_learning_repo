machine learning is the algorythmic part of the data mining process

gli algoritmi che useremo saranno generali, nel senso che possono essere utilizzati senza modifiche in vari domini. Verranno specializzati caso per caso mediante ... [9:46]

# Categorizzazione delle attività di machine learning

reinforcement learning non considerato da noi

- un po' più di nicchia

### Tasks

classification

regression: simile a classification in quanto è comunque una predizione, ma richiede tecniche diverse

similarity matching: DATO UN ELEMENTO, trova quelli simili

clustering: raggruppa elementi simili

profiling

data reduction: simplify data and extract only relevant information

# supervised vs unsupervised learning

Being supervised or unsupervised is a characteristic of the problem and/or the data, it is not a design choice

two main origins of supervised information:

- experts
- history

###

why not java or c++?

- python is more suitable for rapid prototyping
- python has better math libraries and support

# What is a data set?

Narrow view

- a set of N individuals
- each individual is described by D values
- in essence it could be seen as a relational table with N rows and D columns

Broader view

- all the rest
- in most of the cases data are not so nicely arranged
- many machine learning techniques require that the dataset is provided as a relational table
  - transformation
  - preprocessing gives us this nice table
- we will see examples of data sets with different formats and of transformations

# issues on data

tabella slide 6 super importante

descriptive statistics = measures that describe status of something

- stuff like mean, median, variance, ...

```
sinceramente come sono state spiegate le diverse categorie di dato non è chiarissimo. Fai prima a cercare online
```

set means no ordering

interval data are numbers but not quite. They miss a unique zero

ratio kind of data have a meaningful answer to questions like is a twice as much as b?

### allowed transformations

...

### General characteristics of data sets

Un attributo asimmetrico è un tipo di attributo binario (cioè con due valori: 0/1, vero/falso, sì/no) in cui solo la presenza (1) è considerata informativa, mentre l’assenza (0) non è interessante.

- e.g esame passato -> asimmetrico; sesso: m/f -> simmetrico
- **In particular, binary asymmetric attributes are relevant in the discovery of association rules**

...

interessante i fatto che un dato null possa significare due cose:

- non so la targa della macchina
- so che la targa non esiste

...

transaction -> e.g. a basket of items at the supermarket

...

# Data Quality

- Which are the problems?
  - noise and outliers
  - missing values
  - duplicates
  - inconsistencies
- How can we detect the problems?
- What can we do about these problems?

...

outliers can be generated from a rare event or from noise... it's not easy to distinguish between the two cases

...

### Detecting outliers tramite inter-quartile-range

Questa tecnica si basa sulla suddivisione dei dati in quartili:

- Q1 (primo quartile): il 25% dei dati è sotto questo valore
- Q2 (mediana): il 50% dei dati è sotto questo valore
- Q3 (terzo quartile): il 75% dei dati è sotto questo valore

L’IQR (InterQuartile Range) rappresenta l’ampiezza della parte centrale dei dati: IQR=Q3−Q1

- Misura la dispersione dei dati senza farsi influenzare dagli outlier.
- L’idea è che i valori troppo lontani dal “cuore” della distribuzione siano probabilmente outlier.

Si definiscono due limiti (boundary):

- Lower Boundary: Q1 − 1.5*IQR
- Upper Boundary: Q3 + 1.5*IQR

Un valore è considerato outlier se:

- è più piccolo del limite inferiore, oppure
- è più grande del limite superiore

Nei boxplot:

- la scatola va da Q1 a Q3
  - la linea dentro la scatola è la mediana (Q2)
- i whisker (baffi) arrivano fino all’ultimo valore dentro i bondary
- i valori fuori dai baffi sono segnati come outlier (puntini)
