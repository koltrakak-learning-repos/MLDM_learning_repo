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

# Feature selection

...

## The curse of dimensionality

al crescere del numero di features (dimensionalità), algoritmi che discriminano in base a distanze, diventano sempre meno efficaci

- In alta dimensionalità, la distanza massima e quella minima tra punti tendono ad avvicinarsi.
- Le distanze perdono significato

### Filter and Wrapper methods

Nella Feature Subset Selection esistono diversi modi per scegliere un sottoinsieme di attributi utili a migliorare prestazioni, e generalizzazione di un modello.

```
dependant variable == variabile che vogliamo predire (che ci si aspetta dipenda in qualche modo dalle feature)
```

Filter e Wrapper — rappresentano due grandi famiglie di tecniche per questo scopo

**Filter Approaches**

I filter selezionano le feature prima dell’applicazione di qualsiasi algoritmo di data mining o machine learning.

Esempio: Correlation-based selection -> si scelgono le feature più correlate con la target.

**Wrapper approaches**

I wrapper selezionano le feature utilizzando direttamente il modello come “valutatore”. Per ogni sottoinsieme testato, il modello viene addestrato e valutato: il sottoinsieme che produce le performance migliori viene scelto

### Difference between Filter and Wrapper methods

- Filter methods measure the relevance of features by their correlation with dependent variable
- while wrapper methods measure the usefulness of a subset of feature by actually training a model on it

...

in the last line there's obvious relationship between the features but the correlation is 0

- this is because of simmetry and non-linear relationships

## dimensionality-reduction

Instead of considering which subset of attributes is to be ignored it is possible to map the dataset into a new space with fewer attributes

### PCA Principal Component Analysis

```chatgpt
In PCA, **“capturing the variability of the data”** significa:

➡️ **Rappresentare quanta parte dell’informazione contenuta nei dati originali riusciamo a mantenere proiettandoli su una nuova direzione (una nuova dimensione).**

### Più concretamente:

* La **variabilità** è misurata tramite la **varianza**.
* Una direzione (o principal component) **cattura molta variabilità** se, quando proiettiamo i dati su quella direzione, i valori proiettati mostrano **alta varianza**.
* Alta varianza = punti più “sparpagliati” lungo quella direzione → quella direzione contiene molta informazione sulla struttura dei dati.
* Proiettare i dati su una direzione significa considerarne solo la componente relativa a quella direzione


Le nuove dimensioni create dalla PCA:

1. Sono ordinate dalla maggiore alla minore varianza catturata.
2. Le prime poche componenti spesso spiegano la maggior parte dell’informazione utile nei dati originali.
3. Questo permette di ridurre la dimensionalità senza perdere troppo contenuto informativo.

### Un esempio intuitivo

Immagina un insieme di punti disposti come un’ellisse molto allungata:

* La direzione dell’asse lungo dell’ellisse ha molta variabilità → **prima componente principale**.
* La direzione corta ne ha meno → **seconda componente**.

Se proietti i dati sulla prima direzione, preservi già gran parte della forma dell’ellisse → hai **catturato molta variabilità**.

In breve: **"Catturare la variabilità" = mantenere quanto più possibile la varianza dei dati originali quando li rappresenti in meno dimensioni.**

INOLTRE

In PCA non utilizzi le direzioni già presenti nel dataset (cioè gli assi originali degli attributi).
👉 Devi calcolare delle nuove direzioni, chiamate componenti principali.

Gli assi originali non sono scelti per massimizzare la variabilità. Sono solo le coordinate in cui i dati sono stati raccolti.

PCA cerca invece le direzioni “migliori” per descrivere i dati, cioè: quelle lungo cui i dati variano di più (massima varianza) e che siano tra loro ortogonali (indipendenti)

Per calcolare queste nuove direzioni si fanno delle operazioni sulla matrice di covarianza e analisi sui suoi autovettori/valori
```

PCA è computationally intensive, esistono forme approssimate più fattibili per dataset grandi

## MultiDimensional Scaling

tecnica di visualizzazione

MDS is a technique used to visualize high-dimensional data in a low-dimensional space

Fits the projection of the elements into a m dimensional space in such a way that the distances among the elements are preserved

# Scikit-learn

score, quanto è importante la feature per il target

pvalue = misura di quanto lo score è affidabile

- es: lancio una moneta 10 volte e ottengo 9 teste e 1 croce. p(testa) = 0.9?
- l'affidabilità dipende dal numero di volte che lancio la moneta. Il pvalue mi dà una misura di affidabilità che in questo caso dipende dal numero di lanci

## Recursive Feature Elimination Wrapper Method
