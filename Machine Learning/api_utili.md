# Generali

- display() per visualizzazione di jupyter

- list() per trasformare roba simile ad una lista in una lista (iterable, df.columns, ...)

- .append() e .remove() per le liste
  - funzionano in place

# Pandas

## Dataframe

- df.shape
  - .shape\[0] per numero di righe, shape\[1] per numero di colonne

- df.describe(include="all")
  - fornisce informazioni utili come count, nunique, max e min con cui puoi vedere se ci sono dei missing values e roba

- df.info()
  - mostra i tipi delle colonne e il count dei non-null per ciascuna colonna

- df.value_counts(target)
  - restituisce una serie con i counts dei valori dell'attributo passato

- df.columns
  - per ottenere la lista dei nomi delle colonne
  - se non è presente nel dataset posso specificarla io quando leggo
    - header = \['sepal length', 'sepal width', 'petal length', 'petal width', 'class' \]; df = pd.read_csv(url, names=header)

- corr = df.corr()
  - per calcolare la matrice di correlazione

- df.copy()
  - copia profonda del df
  - conviene farle in modo da poter confrontare i cambiamenti senza refreshare jupyter
  - fai df2, df3, ...

- df.dropna()
  - per droppare le righe che contengono un null
  - puoi fare così `df.shape[0] - df.dropna().shape[0]` per controllare quante righe null c'erano

- df.notna()
  - per ottenere un dataframe maschera booleana con la stessa forma del dataframe di partenza

- df.drop()
  - Drop columns  -> df.drop(['B', 'C'], axis=1)
  - or rows       -> df.drop([0, 1])
  - con questo metodo è molto utile ricordardi che le Series hanno un attributo index:
    - df4 = df4.drop( df4\[df4\["InvoiceNo"].str.startswith("C")].index )

- df.sort_values(by=column, ascending=False)
  - per ordinare le righe di un dataframe secondo il valore di una colonna

- df.nunique()
  - restituisce una serie con il numero di valori unique per ogni colonna

- df5.groupby(\["InvoiceNo", "Description"]).sum()
  - groupby serve a raggruppare le righe che hanno lo stesso valore per uno o più attributti e poi applicare un’operazione (come sum, mean, count, ecc.).
  - se raggruppo per più attributi, ottengo un indice multidimensionale
  - dopo aver raggruppato posso anche decidere di applicare la mia operazione per i gruppi so sottoporzioni delle colonne
    - df5.groupby(\["InvoiceNo", "Description"])\["Quantity"].sum()

- df.groupby(\["InvoiceNo", "Description"])\["Quantity"].sum().unstack()
  - unstack serve a spostare l'ultimo indice di riga e a farlo diventare un indice di colonna.
  - Facendo unstack abbiamo spostato le N Description di ogni InvoiceNo in N colonne.
  - L'indice diventa così unidimensionale e, per le Description di un determinato InvoiceNum
    - nella sua colonna abbiamo il valore della somma che c'era presente prima,
    - per le Description non presenti per un determinato InvoiceNo abbiamo invece NaN

- basket_sets = basket.map(encode_units)
  - applica una funzione a tutti gli elementi del dataframe
  - def encode_units(x): return x >= 0

- basket2.astype("bool")
  - per cambiare il tipo di tutte le colonne di un dataframe

### Plotting dataframes

- df.plot(x="lift", y="confidence", kind="scatter")

- df.hist()
  - plotta un istogramma per tutte le colonne
  - plt.hist(df\[target\]); invece plotta solo una singola colonna

## Series

Tutta questa roba vale anche quando si accede ad una colonna di un dataframe con df\["col"]

- series.idxmax(axis=0)
  - per ottenere la riga di una serie con valore maggiore
  - tipicamente si usa quando si vuole cercare la riga migliore di un df
    - best_row = results.loc\[results.scoring==scoring_filter, scoring_filter].idxmax(axis=0)

- series.unique()
  - restituisce un array con i valori unique della serie

- series.nunique()
  - restituisce il numero di valori unique nella serie

### Accesso al contenuto del dataframe

- results = pd.DataFrame(columns=['scoring', 'model', ...\])
  - per creare un dataframe con determinate colonne

- results.loc\[len(results)] = \[ score, model\['name'], ... ]
  - per appendere una riga in fondo ad un dataframe

- results.scoring=="accuracy"
  - per ottenere una serie di valori booleani che fa da maschera ad un dataframe
  - la maschera ha valore True solo per le righe del df in cui l'attributo scelto ha quel valore

- results\[results.scoring=="accuracy"]
  - per ottenere un dataframe filtrato dall'applicazione della maschera

- results\[~(results.scoring=="accuracy")]
  - puoi usare l'operatore ~ per negare la maschera e quindi filtrare con logica negativa

- results.loc\[results.scoring=="accuracy","accuracy"]
  - posso usare loc anche per ottenere una serie da una colonna di un dataframe fornendo un secondo indice (per la colonna da scegliere)
  - posso anche usare una lista di colonne: results.loc\[2, \["linkage", "n_clusters"]]

- df_test_sorted\["uni_pred"] = uni_pred
  - mi permette di aggiungere una colonna ad un dataframe

# Matplotlib

NB: there are 2 ways to use matplotlib

- Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").
- Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot functions for plotting.

- fig = plt.figure()
  - an empty figure with no Axes
    - verranno aggiunti automaticamente con metodi come plt.plot(), ...
  - **usato con pyplot style**

- plt.scatter(X\[feature], y)
  - permette di disegnare uno scatterplot su un plt.figure() o su un plt.subplot()

- plt.subplot(rows, cols, i)
  - permette di disegnare una griglia (rows*cols) di subplot con i indice di subplot
  - alla prossima chiamata di plt.scatter(), plt.plot(), ... si disegnerà nell'ultimo subplot chiamato

- plt.pie(counts=clust_sizes_km\[1], labels=clust_sizes_km\[0], autopct='%1.1f%%')
  - disegna un pie chart

- fig, ax1 = plt.subplots()
  - **usato con OO syle**
  - crea una nuova figura e uno o più assi (gli “spazi” in cui si disegnano grafici).
  - Restituisce due oggetti:
    - fig → l’oggetto Figure -> È la “pagina” o il contenitore generale che può contenere uno o più grafici.
    - ax1 → l’oggetto Axes (plurale) -> È l’area effettiva in cui viene tracciato il grafico (assi X e Y, titoli, curve, ecc.).
  - the Figure keeps track of all the child Axes
  - ax serve per disegnare il grafico
    - ax1.plot(x, y)
    - ax1.set_title("Titolo")
    - ax1.set_xlabel("X")
  - NB: Axes non gestisce solo gli assi (che nome...), rappresenta tutto il riquadro del grafico invece
  - se passo nrow ed ncol: fig, ax = plt.subplots(2, 2)
    - ax diventa un array di Axes (in questo caso 2x2), ognuno dei quali mi rappresenta un riquadro in qui disegnare il mio plot

- ax2 = ax1.twinx()  
  - instantiate a second axes that shares the same x-axis

# Scikit learn

Most commonly, the steps in using the Scikit-Learn estimator API are as follows

1. Choose a class for the model by importing the appropriate estimator class from Scikit-Learn.
2. Choose model hyperparameters by instantiating this class with desired values.
3. Arrange data into a features matrix ``X`` and target vector ``y``
4. Fit the model to your data by calling the ``fit()`` method of the model instance.
5. Apply the Model to new data:
   - For **supervised learning**, often we predict labels for unknown data using the ``predict()`` method.
   - For **unsupervised learning**, we often transform or infer properties of the data using the ``transform()`` or ``predict()`` method.

- Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=random_state, train_size=0.67)

## Model selection con crossvalidation

### Tuning degli iperparametri di un modello

```python
# dobbiamo preparare una mappa in cui ogni elemento contiene
# una lista di tutti i valori di parametro che vogliamo tunare
# per il classificatore
param_grid = {
    'max_depth': [*range(1,fitted_max_depth+1)],
    'criterion' : ['entropy', 'gini'],
    'class_weight' : [None, 'balanced']
}

```

```python
# e poi dobbiamo preparare una lista di tutti gli
# score che vogliamo usare per la valutazione 
# della configurazione di iperparametri migliore
scores = [
    'precision_macro',
    'precision_weighted',
    'recall_macro',
    'recall_weighted',
    'f1_macro',
    'f1_weighted',
    'accuracy'
]
```

A questo punto possiamo chiamare `GridSearchCV()` (guarda su scikit-learn docs)

```python
# cerchiamo gli iperparametri che ottimizzano ogni score
for score in scores:
    grid = GridSearchCV(
        model, # the estimator will be refitted
        param_grid,
        scoring=score,
        cv=5 # numero di crossvalidation folds
    )
    # the fit method of a GridSearchCV will do the crossvalidation
    # and the looping on all the combination of hyperparameters in
    # the parameters grid
    grid.fit(Xtrain, ytrain)
    # dopo il fitting abbiamo a disposizione un po' di roba (tutta presente nelle docs)
    print(grid.best_params_)
    print(grid.best_estimator_)
    print(grid.best_score_)
    # possiamo utilizzare il modello trovato come prima con .predict()
    ypred = grid.best_estimator_.predict(Xtest)
```

### Model selection con vari modelli

``` python
# come sopra ho bisogno di preparare un po' di roba.
# Inizio con le label che userò come chiavi nella mappa che contiene i modelli
model_labels = [
    'dt', # decision tree
    'nb', # naive bayes
    ...
]

# preparo una mappa in cui ogni elemento è un altra mappa che contiene
# estimator e parameter_grid di un modello
models = {
    'dt': {
        'name': 'Decision Tree',
        'estimator': DecisionTreeClassifier(random_state=random_state), 
        'param': [
                    {
                        'max_depth': [*range(1,20)],
                        'class_weight':[None,'balanced']
                    }
        ],
    },
    'nb': {
        'name': 'Gaussian Naive Bayes',
        'estimator': GaussianNB(),
        'param': [
            {
                'var_smoothing': [10**exp for exp in range(-3,-13,-1)]
            }
        ]
    },
    ...
}

# e come prima ho bisogno anche di una lista con tutti i miei metodi
# di scoring che voglio usare per trovare la configurazione di iperparametri
# migliore di ogni modello
scores = [
    'precision_macro',
    # 'precision_weighted',
    'recall_macro',
    # 'recall_weighted',
    'f1_macro',
    # 'f1_weighted',
    'accuracy'
]
```

```python
# mentre sopra cercavo il best model (migliore configurazione di iperparametri)
# per ogni score e basta.
# Adesso cerco il best model per ogni score e per ogni modello! Il procedimento 
# però è sostanzialmente lo stesso
for score in scores:
    for model_label in model_labels:
        model = models[model_label]
        
        clf = GridSearchCV(
            model['estimator'],
            model['param'],
            scoring=score,
            cv=5
        )
        # the fit method of a GridSearchCV will do the crossvalidation
        # and the looping on all the combination of hyperparameters in
        # the parameters grid
        clf.fit(Xtrain, ytrain) 
        y_pred = clf.best_estimator_.predict(Xtest)
```

## Regressione

siccome anche questo è un task supervisionato si usano sempre i metodi  `fit()` e `predict()`  sull'estimator che farà la regressione

- stavolta il fitted estimator ci da a disposizione i suoi pesi con:
  - weight_uni = univariate_estimator.coef_\[0]
  - intercept = univariate_estimator.intercept_

## Clustering

- kmeans = KMeans(k, random_state=random_state); labels = kmeans.fit_predict(df)
  - essendo un task unsupervised non ho neanche bisogno di fare training con fit o di splittare in trainset e testset

- pg = ParameterGrid(parameters)
  - produce una lista di mappe in cui ogni mappa rappresenta una combinazione dei parametri possibile
  - utile in clustering quando si vuole vedere quale configurazione di parametri (es: eps e n_min in DBSCAN) produce il clustering migliore

- DBSCAN(parameter_conf\["eps"], min_samples=parameter_conf\["min_samples"]).fit_predict(df)
  - ha degli attributi utili una volta fittato
    - db.n_clusters_
    - db.n_noise_
  - i punti classificati come rumore hanno come label: -1
    - puoi rimuovere gli outlier con: db_labels\[db_labels != -1]

## preprocessing

- pol_feat = PolynomialFeatures(degree=2, include_bias=False)
  - questo permette di creare nuove feature che sono potenze di feature già presenti
  - X_train_poly = pol_feat.fit_transform(X_train); X_test_poly = pol_feat.fit_transform(X_test)

- pt = PowerTransformer()
  - permette di rendere meno skewed alcune distribuzioni di dati rendendole più gaussiane
  - df\[df.columns\[2:]] = pt.fit_transform(df\[df.columns\[2:]])

- scaler = MinMaxScaler(feature_range=(0, 1))
  - scala le features linearemente nel range spcificato
  - df\[df.columns] = scaler.fit_transform(df\[df.columns])

- le = LabelEncoder()
  - permette di passare da categorical features a integer features assegnando interi successivi da 0 a n-1
  - y = le.fit_transform(df_train\[target])

- pca = PCA()
  - permette di trasformare le features in principal components già ordinati per varianza spiegata
  - X_trans = pca.fit_transform(X_full)
  - il fitted object ha come attributo un array in cui ogni elemento contiene la percentuale di varianza spiegata: `pca.explained_variance_ratio_`

- selector = SelectKBest(mutual_info_classif, k=k_best)
  - permette di selezionare le k feature migliori secondo uno score che le feature hanno con il target
  - X_train = selector.fit_transform(X_train_full, y_train)

## roba per valutazione dei modelli

- test_set_accuracy = accuracy_score(ytest, ytest_dt)
  - to see the fraction of predicted training set labels that match their true value.

- print(classification_report(ytest, ypred, zero_division=0))
  - questo stampa gli score principali e anche le versioni macro, weighted

- cm = confusion_matrix(ytest, ypred)
  - come dice il nome stampa la confusion_matrix
  - visualizzabile con:
    - disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=grid.classes_)
    - disp.plot()

- mean_squared_error(y_test, y_pred) e r2_test = r2_score(y_test, y_pred)
  - per valutare le predizioni di un regressore

- kmeans.inertia_e silhouette_score(df, labels)
  - autoesplicativi

- pair_confusion_matrix = pair_confusion_matrix(km_labels, agg_labels)
  - computa la pair_confusion_matrix; utile per confrontare due clustering scheme diversi
  - restituisce una matrice 2x2 numpy, posso fare .sum() e accedere agli elementi singolarmente
    - utile se voglio cacolare ade esempio la percentuale di match

# Numpy

- np.arange(1, 10, 1)
  - restituisce un array contenente tutti gli elementi (estremo escluso)

- np.linspace(1, 10, 10)
  - mi divide l'intervallo da 1 a 10 in 10 elementi equidistanti, estremo incluso

- clust_sizes_km = np.unique(labels,return_counts=True)
  - restituisce l'array ordinato di elementi unique nell'array passato
  - può restituire array aggiuntivi in base ai parametri passati; tra i più utili è il count di ogni unique element

- np.asarray(null_mask)
  - trasforma oggetti vari come serie e dataframe in array numpy
  - utile se vuoi ad esempio contare gli elementi di una serie: n_false, ntrue = np.unique(np.asarray(null_mask), return_counts=True)

- array.sort()
  - ordina gli elementi inplace

- cum_variances = np.cumsum(pca_variances)
  - permette di ottenere un array della stessa shape in cui ogni elemento è la somma cumulata dei precedenti
  - chiaramente utile con PCA

- cumulative_variances > pca_threshold
  - espressioni condizionali con array numpy producono array maschere in cui ogni elemento è true/false in base a se l'elemento nell'array rispetta o meno la condizione

- cutoff_index = np.argmax(cumulative_variances > pca_threshold)
  - argmax permette di trovare l'indice del valore più grande nell'array
  - il primo se ce ne è più di uno

# Seaborn

- sns.pairplot(df, hue=target)
  - per visualizzare il pairplot

- sns.heatmap(corr, annot=True)
  - per visualizzare la matrice di correlazione

- sns.boxplot(df, x=target, y=predictor)
  - per visualizzare un boxplot per valore del target vedendo la variazione del predictor corrente
  - sns.boxplot(df\[c\])
    - questo visualizza il boxplot che descrive come varia questa singola colonna del dataframe
