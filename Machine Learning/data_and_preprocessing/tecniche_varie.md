we have many different kind of problems in data and we need to do something about it

also, the type of data may not be adequate

how can i decide when to just drop the row/column instead of inferring the datapoint?

...

# Data type conversions

...

### Ordinal to numeric

with this conversion we're adding an unwanted semantic. We're defining how much better ok is better than awful etc.

This can change the behaviour of a classifier. For example:

- knn is affected
- decision trees aren't affected

### Discretization

The choice of the (optimal) thresholds can emerge from data

- equal width: mi basta decidere il numero di buckets
  - this choice doesn't respect the data!
  - we're putting in the same bucket datapoints conceptually belonging to different sets
- equal frequency:
  - se ho 100 datapoints, e voglio 4 buckets, metto i primi 25 nel primo bucket, e così via
  - un po' meglio di prima ma di nuovo non rispetta granchè i dati se la distribuzione è sbilanciata
- k-means: fuoco

# Sampling

Se il mio dataset è enorme, lavorare con il dataset nella sua interezza potrebbe essere troppo costoso

Una buona idea è lavorare inizialemente con un sottoinsieme del dataset ottenuto tramite sampling, ad esempio per la stima degli iperparametri.

Una volta soddisfatti con i risultati sul sample si può passare all'intero dataset

In general, we will consider sampling without replacement (vedi splitter per crossvalidation)

### Sample size relation with missing class

nel caso di training-test split con crossvalidation è importante considerare la dimensione dei singoli bucket ottenuti da crossvalidation nel training set

- devono essere abbastanza grandi da contenere con buona probabilità almeno una istanza per ogni classe
- **questo ci aiuta a definire il numero di bucket nella crossvalidation**

# Feature creation

...

**NB**: New features: e.g. volume and weight to density

- questo può essere importante dato che la densità non è ottenuta da una relazione lineare tra peso e volume
- molti classificatori però combinano linearmente peso e volume per fare le loro scelte
- se la densità fosse una feature importante del mio problema, senza fare feature creation il modello non riuscirebbe a classificare utilizzando questa metrica
  - non riesce a fare decisioni basate su densità combinando linearmente peso e volume

moving average reduces the random effect in data (in particular for time related information)

...

# Data transformation

the scale of the features can influence machine learning techniques

- algorythms that are influenced by distance
- algorythms that use gradient descent

- min-max scaling
- stadardization
  - less influenced by outliars
- funzioni qualsiasi
  - tipicamente cambiano la distribuzione dei dati

  Normalization è un termine overloaded
  - spesso fa riferimento al MinMaxScaler
  - in scikit-learn normalizza each data-row to unit norm

Nota: min-max scaling should always be done when using neural networks (non ha spiegato perchè ma mi fido)

# Imbalanced dataset

tipically underepresented classes have little influence on the performance of the model

this is a problem if i'm interested on the performance on minority classes

...

we can weigh the classes in our classifiers (?)

- vedi estimators in scikit-learn

oversampling

- we consider examples of underepresented classes many times
- we do not introduce new information

data augmentation

- we synthetize new plausible data for underepresente classes

**NB**: with oversampling, undersampling and data augmentation it's important to not touch the test set because we want to measure performance on real data

undersampling selects horizontal portions of the data

feature selection select vertical portions of the data
