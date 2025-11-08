# premessa

con tutte queste varianti di modelli viene spontaneo chiedersi quale sia il migliore...

purtroppo, la risposta è dipende (nel senso che il migliore non esiste)

# Naive Bayes Classifier

Approccio probabilistico di classificazione. Chiamato in questo modo dato che is basa sul teorema di Bayes di probabilità

Abbiamo visto che i decision tree non sono un parametric classifier

- we don't make any probabilistic assumption

...

l'ipotesi è l'appartenenza ad una classe

l'evidence è una serie di attributi con determinati valori

noi siamo interessati a P(H|E) -> la probabilità di una classe dati quei valori degli attributi

**IMPORTANTE**: facciamo l'ipotesi (facilemente non vera) che gli attributi sono tutti indipendenti e quindi la probabilità che due attributi abbiano determinati valori è il prodotto delle probabilità

- per questo motivo si chiama naive, l'assunzione è molto simplicistica, però funziona!

**Problema**:
attributi con valore 0 fanno crollare la probabilità di una determinata classe a 0 (abbiamo un prodotto)

- per risolvere applichiamo Laplace smoothing

Problema:
se ho dei valori reali non posso calcolarne la frequenza

# Linear Perceptron

con un singolo perceptron riusciamo a definire degli iperpiani

e quindi riusciamo a risolvere solo binary problems

...

it's not guaranteed that the problem has a solution

- data may be not linearly separable

# Suport Vector Machines

again, we're considering binary classification

what can we do if the data isn't linearly separable?

**Maximum margin hyperplane**

- a bigger margin is better at dealing with new data, not included in the training set, similar to the training data
- it maximizes the probability of correct classification (generalizes better)

The support vectors ease the computation of the maximum margin hyperplane

- they are data point that define the perimeter of a particular polygon representative of a class

## Soft margin

optimal margin -> allows us to generalize

soft margin -> allows us to tolerate exceptions

if the separating hyperplane doesn't exist, or is extremely narrow

C is the penalty parameter (hyperparameter) that decides the importance of exceptions

## Kernel trick

we add a dimension to linearly separate

# Neural Networks

by combining neurons we can define decision surfaces different from an hyperplane

...

there is a huge difference between NNs and DTs. The latter are understandable whereas the former are not.

- in DTs the nodes are decisions
- in NNs the nodes are numeri processors

## Universal approximator

this is a theorem:

a NN with a hidden layer, and an activation function that is not linear, is able to approximate any function

- theorem of existence, this doesn't tell us how to do it

# Instance Learning or K-nearest neighbour classifier

consider the distance between the new example and the examples i've trained on

choose the class of the majority of the k-nearest neighbours

the model is the training set itself

ci sono degli iperparametri

- quanto lontano guardo?
- k
- metrica con cui misurare la distanza

# From a binary classifier to multi-class classification

Several classifiers (e.g. SVM and linear perceptron), generate a binary classification model. But what if we want to use these classifiers for multi-class classification?

Two ways to deal with multi–class classification:

- transform the training algorithm and the model
  - sometimes at the expenses of an increased size of the problem
- use a **set of binary classifiers** and combine the results
  - at the expenses of an increased number of problems to solve

**OVO**
consider all the possible pairs of classes and generate a binary classifier for each pair

- C*(C-1)/2 pairs
- each binary problem considers only the examples of the two selected classes

at prediction time apply a voting scheme

- the class with the highest number of +1 wins
- an unseen example is submitted to the  C*(C-1)/2 binary classifiers
  - each winning class receives a +1
  - molte coppie non considerano neanche la classe corretta tra le due tra cui distinguono e quindi emetteranno un risultato per forza sbagliato
  - poco male, l'importante è che le C-1 coppie che contengono la classe corretta classifichino correttamente

**OVR**
consider C binary problems where class c is a positive example, and all the others are negatives

- build C binary classifiers, dove ognuno impara a distinguere tra: "questo è c, questo non è c"

at prediction time apply a voting scheme

- an unseen example is submitted to the C binary classifiers, obtaining a confidence score
- the confidences are combined and the class with the highest global score is chosen

**OVO vs OVR**

- OVO requires solving a higher number of problems, even if they are of smaller size
- OVR tends to be intrinsically unbalanced
  - if the classes are evenly distributed in the examples, each classifier has a proportion positive to negative 1 to C ´ 1

# Ensemble methods

the quality of many INDIPENDENT classifiers, is better than that of one single classifiers

- that's what probability tells us (vedi slide 110)

- if the base classifiers are equal (the same classifier), the ensemble error rate is still epsilon
  - tutti mi danno lo stesso risultato
- if the base classifiers have all error rate epsilon, but they are independent (their errors are uncorrelated) then **the ensemble will be wrong only when the majority of the base classifier is wrong**

But, is it easy to obtain many different INDIPENDENT classifiers?

- the answer is no

One way is to choose different subsets of predicting attributes for different classifiers

- this done for example by the random forest classifier that combines many indipendent decision trees

In general we have to **manipulate the training set**:

- bagging
  - crea molti classificatori addestrandoli su sottocampioni casuali del dataset
  - si genera un nuovo dataset per ciascun classificatore, campionando il training set con una distribuzione uniforme

- boosting
  - costruisce i classificatori in modo sequenziale, ogni nuovo classificatore cerca di correggere gli errori commessi dai precedenti.
  - come funziona:
    - si inizia con una distribuzione uniforme dei dati nel training set e si addestra il primo classificatore.
      - (immagino si campioni anche qua)
    - iteratively changes the distribution of training examples so that the base classifier focus on examples which are hard to classify
  - **Adaboost**: the importance of each base classifier in the final classification depends on its error rate
