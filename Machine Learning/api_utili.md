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

### Accesso al contenuto del dataframe

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
3. Arrange data into a features matrix and target vector following the discussion above.
4. Fit the model to your data by calling the ``fit()`` method of the model instance.
5. Apply the Model to new data:
   - For **supervised learning**, often we predict labels for unknown data using the ``predict()`` method.
   - For **unsupervised learning**, we often transform or infer properties of the data using the ``transform()`` or ``predict()`` method.

- Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=random_state, train_size=0.67)

## roba per valutazione dei modelli

- test_set_accuracy = accuracy_score(ytest, ytest_dt)
  - to see the fraction of predicted training set labels that match their true value.

# Seaborn

- sns.pairplot(df, hue=target)
  - per visualizzare il pairplot

- sns.heatmap(corr, annot=True)
  - per visualizzare la matrice di correlazione

- sns.boxplot(df, x=target, y=predictor)
  - per visualizzare un boxplot per valore del target vedendo la variazione del predictor corrente
  - sns.boxplot(df\[c\])
    - questo visualizza il boxplot che descrive come varia questa singola colonna del dataframe
