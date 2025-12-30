# Feature selection

why is it used?

1. Sometimes less is more:
    - It can enable the machine learning algorithm to train faster
        - ad esempio, mitiga curse of dimensionality dato che fa **dimensionality reduction**
        - oppure, semplicemente dato che ci sono meno colonne reduces time and memory complexity of the mining algorithm
    - It can reduce the complexity of a model and makes it easier to interpret (eg. with visualizations)
    - It can improve the accuracy of a model if the right subset is chosen
    - **It can reduce overfitting**
        - eliminando feature non importanti/non predittive quest'ultime non possono venire imparate e non possono portare a predizioni sbagliate

2. Some attributes can be problematic
    - may be redundant if correlation between the two is high
    - can be misleading ... non ci interessa come
    - **è bene tagliare via alcuni attributi problematici, una sorta di data cleaning**

### The curse of dimensionality

al crescere del numero di features (dimensionalità), algoritmi che discriminano in base a distanze, diventano sempre meno efficaci

- In alta dimensionalità, lo spazio diventa sparsamente popolato (la densità dei punti tende a diminuire)
- questo significa che la distanza massima e quella minima tra punti tendono ad avvicinarsi.
- in altri termini, **le distanze diventa sempre più simili tra di lore -> Le distanze perdono significato**

## Come si fa?

Innanzitutto, possiamo sicuramente:

- eliminare attributi ridondanti
  - sia quelli fortemente correlati tra di loro, che quelli derivabili da altri
- eliminare gli attributi irrilevanti, ovvero quelli che non hanno alcun poter predittivo sul target (vedi codice fiscale e ricchezza)
- eliminare attributi con poco variabilità
  - se è un attributo è più o meno sempre uguale across l'intero dataset allora non serve a molto

Da qui in avanti comincia la parte più di machine learning

### Supervised o unsupervised

feature selection può essere un'attività sia unsupervised che supervised

**Supervised**:

- Filter methods
  - ad esempio: seleziono le feature con un'alta correlation with the target class
- Wrapper methods
- Embedded methods
  - Decision Trees (usano gli attributi che massimizzano l'information gain)
  - Lasso (L1)
  - Elastic Net

**NB**: in quanto supervised tutti questi metodi richiedono le label della target class

**Unsupervised:**

- Possiamo sfruttare clustering
  - Fai clustering (es. k-means) usando tutte le feature
  - Valuti la qualità del clustering
    - silhouette score
  - Rimuovi una feature
  - Rifai clustering
  - Se la qualità non peggiora (o migliora) → la feature è inutile
  - **NB**: questo è un unsupervised wrapper method dato che usa kmeans come valutatore del subset di feature
  - **NB**: Nel supervised dici: “Questa feature è utile perché discrimina le classi” Nel clustering dici invece: “Questa feature è utile perché aiuta a mantenere separati i gruppi naturali di dati”
- Oppure possiamo sfruttare **PCA**
  - questa non è propriamente feature selection, è una combinazione di feature transformation e dimensionality reduction

### Filter and Wrapper methods

Nella Feature selection esistono diversi modi per scegliere un sottoinsieme di attributi utili

Filter e Wrapper — rappresentano due grandi famiglie di tecniche per questo scopo

**Filter Approaches**:

I filter **selezionano le feature prima dell’applicazione di qualsiasi algoritmo machine learning.**

- Esempio: Correlation-based selection -> si scelgono le feature più correlate con il target.

**Wrapper approaches**:

I wrapper selezionano le feature utilizzando direttamente **un modello come “valutatore”.**

- Per ogni sottoinsieme di feature da testare, il modello viene addestrato e valutato
  - nota come questo sia molto **computazionalmente costoso** rispetto a filter methods
- il sottoinsieme che produce le performance migliori viene scelto

**Embedded Methods**:

Feature selection occurs naturally as part of the data mining algorithm

- e.g. decision trees oppure con Lasso regression

**Difference between Filter and Wrapper methods** (nel nostro caso):

```
dependant variable == variabile che vogliamo predire (che ci si aspetta dipenda in qualche modo dalle feature)
```

- Filter methods measure the relevance of features by their correlation with dependent variable
- wrapper methods measure the usefulness of a subset of feature by actually training a model on it

## Our correlation-based filter method

Correlation zero == absence of **linear** relationship between the variables

- limitation!
- the relationship might not be linear
  - nella slide 74, in the last line, there's obvious relationship between the features but the correlation is 0

We're going to use correlation this way:

- Identifying Redundant Features for Dimensionality reduction
  - Features highly correlated with each other contain overlapping information
  - Retain one feature from such groups to reduce dimensionality and overfitting

- Identifying Relevant Features (filtering)
  - High correlation with the target variable helps identify features with high predictive power
  - **NB**: low correlation between a feature and the target **can sometimes hide a non–linear correlation**, therefore the mere use of low correlation for feature filtering can be dangerous
    - correlation should be complemented with other techniques to handle nonlinear relationships (non mi sembra però che abbiamo visto queste altre tecniche)

## Recursive Feature Elimination | Wrapper Method

RFE involves the following steps:

- Step 1: Train a model on all features of the dataset.
- Step 2: Rank features by importance
  - Based on the trained model, rank all features by their importance using model coefficients or feature importance scores
- Step 3: Remove the least important feature(s)
  - The model is retrained with the remaining features.
- Step 4: Repeat steps 1–3 until the desired number of features is reached

**NB**: Wrapper methods measure the usefulness of a subset of feature by actually training a model on it

- Filter methods might fail to find the best subset of features in many occasions but wrapper methods can always provide the best subset of features
- tuttavia computationally expensive and no always easy to rank feature importance

# dimensionality-reduction

Instead of considering which subset of attributes is to be ignored it is possible to map the dataset into a new space with fewer attributes

**NB**: questa è una trasformazione dei dati, non più una semplice selezione

## PCA, Principal Component Analysis

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

# Feature selection in Scikit-learn e cose pratiche che interessano a noi

## Univariate feature selection

È una tecnica di feature selection supervisionata.

- Supervisionata perché usa il target (la variabile da predire).

“Univariate” significa che:

- ogni feature viene analizzata da sola
- si studia la relazione feature ↔ target
- non considera interazioni tra feature

Per ogni feature:

- applica un test statistico -> nel nostro caso correlazione
- ritorna:
  - uno score → quanto la feature è informativa nel predirre il target
  - un p-value → quanto il risultato è statisticamente significativo/affidabile

Infine, si selezionano le k feature con score migliore / una percenutale delle feature con score migliore

### p-value

It is the probability that the null hypothesis is acceptable

- the null hypothesis is that there is **no relationship between the feature and the target**

Il p-value serve a rispondere alla seguete domanda:

`Se in realtà NON esistesse alcuna relazione tra X e y, quanto è probabile osservare una correlazione almeno così forte solo per caso?`

- es: lancio una moneta 10 volte e ottengo 9 teste e 1 croce. Possiamo concludere che p(testa) = 0.9?
- l'affidabilità dipende dal numero di volte che lancio la moneta.
- Il pvalue mi dà una misura di affidabilità che in questo caso dipende dal numero di lanci

Più il p-value è piccolo più la misura è affidabile e non dovuta a casualità
