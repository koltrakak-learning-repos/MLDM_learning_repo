# Generali

- display() per visualizzazione di jupyter

- list() per trasformare roba simile ad una lista in una lista (iterable, df.columns, ...)

- .append() e .remove() per le liste
  - funzionano in place

# Pandas

## Dataframe

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

- df.drop()
  - Drop columns  -> df.drop(['B', 'C'], axis=1)
  - or rows       -> df.drop([0, 1])

- df.sort_values(by=column, ascending=False)
  - per ordinare le righe di un dataframe secondo il valore di una colonna

- series.idxmax(axis=0)
  - per ottenere la riga di una serie con valore maggiore
  - tipicamente si usa quando si vuole cercare la riga migliore di un df
    - best_row = results.loc\[results.scoring==scoring_filter, scoring_filter].idxmax(axis=0)

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

- results.loc\[results.scoring=="accuracy","accuracy"]
  - posso usare loc anche per ottenere una serie da una colonna di un dataframe fornendo un secondo indice (per la colonna da scegliere)

# Matplotlib

NB: there are 2 ways to use matplotlib

- Explicitly create Figures and Axes, and call methods on them (the "object-oriented (OO) style").
- Rely on pyplot to implicitly create and manage the Figures and Axes, and use pyplot functions for plotting.

- fig = plt.figure()
  - an empty figure with no Axes
    - verranno aggiunti automaticamente con metodi come plt.plot(), ...
  - **usato con pyplot style**

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

### Plotting dataframes

- df.hist()
  - plotta un istogramma per tutte le colonne
  - plt.hist(df\[target\]); invece plotta solo una singola colonna

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

# Seaborn

- sns.pairplot(df, hue=target)
  - per visualizzare il pairplot

- sns.heatmap(corr, annot=True)
  - per visualizzare la matrice di correlazione

- sns.boxplot(df, x=target, y=predictor)
  - per visualizzare un boxplot per valore del target vedendo la variazione del predictor corrente
  - sns.boxplot(df\[c\])
    - questo visualizza il boxplot che descrive come varia questa singola colonna del dataframe
