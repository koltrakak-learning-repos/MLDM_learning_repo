we have many different kind of problems in data and we need to do something about it

- Missing values
- Skewed distributions
- Outliers
- Dimensionality
- Errors and duplications

also, the type of data may not be adequate as in we might want numeric data but we have categorical data, o viceversa

- datatype conversions may be necessary

# Missing values

we have to alternatives

- the simplest way to handle missing data is to remove rows or columns containing NaN values.
- the other possibility is imputation with mean or median of the column

how can i decide when to just drop the row/column instead of inferring the datapoint?

- tipicamente droppare una colonna è un po' forte, perdiamo una intera feature
- abbiamo un dataset largo o lungo?

# Data type conversions

why is it needed:

- Many algorithms require numeric features
  - eg: categorical features must be transformed into numeric
- Classification requires a target with nominal values, a numerical (continuous) target can be discretised
- Discovery of association rules require boolean features
  - a numerical feature can be discretised
  - and transformed int a series of boolean features (una per ogni valore discretizzato)

Esempi:

- **Nominal to numeric**: OneHotEncoder
  - trasforma una feature nominale con V valori, in un vettore di V feaure booleane
- **Ordinal to numeric**: OrdinalEncoder
  - The ordered sequence is transformed into consecutive integers
- **Numeric to binary (discretization massima)**: Binarizer
  - Not greater than the threshold becomes zero, Greater than the threshold becomes one
- **Numeric to discrete**: KBinsDiscretizer
  - varie strategie, anche kmeans

### Ordinal to numeric

OSS: with this conversion we're adding an unwanted semantic.

- We're defining how much better ok is better than awful etc.
- ordinal data non hanno una nozione di distanza tra i valori

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

- chiaramente il sample deve essere rappresentativo dell'intero dataset

Una volta soddisfatti con i risultati sul sample si può passare all'intero dataset

In general, we will consider sampling without replacement (vedi splitter per crossvalidation)

### Sample size relation with missing class

nel caso di training-test split con crossvalidation è importante considerare la dimensione dei singoli bucket ottenuti da crossvalidation nel training set

- esiste una formula che ci mostra come i bucket debbano essere abbastanza grandi da contenere con buona probabilità almeno una istanza per ogni classe
  - più è grande il numero di target (classi), più la dimensione del sample deve essere grande per essere rappresentativa
- **questo ci aiuta a definire il numero di bucket nella crossvalidation**

# Feature creation

It involves transforming raw data into meaningful features that can improve predictive models

**esempio**: we can calculate new features -> density from volume and weight

- questo può essere importante dato che la densità non è ottenuta da una relazione lineare tra peso e volume
- molti classificatori però combinano linearmente peso e volume per fare le loro scelte
- se la densità fosse una feature importante del mio problema, senza fare feature creation il modello non riuscirebbe a classificare utilizzando questa metrica
  - non riesce a fare decisioni basate su densità combinando linearmente peso e volume

Altri esempi possono essere:

- Feature extraction: pixel picture with a face -> eye distance, . . .
- Mapping to a new space: signal to frequencies with Fourier transform

# Data transformation

why is it needed:

- the features may have different scales this can alterate the results of many learning techniques
  - pensa a quelle basate su distanze, le feature con scala maggiore renderebbero irrilevanti quelle con scala piccola
- there can be outliers
  - pensa di nuovo alle distanze

## feature transformation

Map the entire set of values of an attribute to a new set according to a function

- min-max scaling
  - applica uno shrinking/stretching lineare ai valori -> la distribuzione non viene modificata
  - spesso scalo in range \[0,1]
- stadardization
  - trasformo una distribuzione gaussiana in una distribuzione gaussiana standard
  - less influenced by outliars
- funzioni qualsiasi
  - tipicamente cambiano la distribuzione dei dati

Normalization è un termine overloaded

- spesso fa riferimento al MinMaxScaler
- in scikit-learn normalizza each data-row to unit norm

Nota: min-max scaling should always be done when using neural networks (non ha spiegato perchè ma mi fido)

# Imbalanced dataset

tipically underepresented classes have little influence on the performance of the model

- **this is a problem if i'm interested on the performance on minority classes**

Per aumentare l'influenza delle underrepresented classes:

- oversampling the minority classes
  - we consider examples of underepresented classes many times
  - we do not introduce new information
  - è quello che succede quando si fa cost-sensitive learning in cui si pesano di più le classi più costose
    - nel nostro caso quelle minoritarie

- undersampling the majority classes
  - otteniamo un dataset bilanciato
  - ma perdiamo della conoscenza nel training set

- data augmentation
  - we synthetize new plausible data for underepresented classes
  - SMOTE is a technique to do so

**NB**: with oversampling, undersampling and data augmentation it's important to not touch the test set because we want to measure performance on real data

OSS:

- undersampling selects horizontal portions of the data
- feature selection select vertical portions of the data
