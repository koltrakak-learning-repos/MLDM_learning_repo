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

set means no ordering

interval data are numbers but not quite. They miss a unique zero

ratio kind of data have a meaningful answer to questions like is a twice as much as b?

Un attributo asimmetrico è un tipo di attributo binario (cioè con due valori: 0/1, vero/falso, sì/no) in cui solo la presenza (1) è considerata informativa, mentre l’assenza (0) non è interessante.

- e.g esame passato -> asimmetrico; sesso: m/f -> simmetrico
...

interessante i fatto che un dato null possa significare due cose:

- non so la targa della macchina
- so che la targa non esiste

...

transaction -> e.g. a basket of items at the supermarket

...

outliers can be generated from a rare event or from noise... it's not easy to distinguish between the two cases
