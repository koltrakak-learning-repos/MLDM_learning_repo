In regression the target is numeric; the goal is forecasting continuous values

response vector == predizione (non necessariamente un vettore se vogliamo predirre solamente una variabile)

# Linear regression

i pesi che impariamo sono numerosi tanto quanto il numero di feature del dataset

la predizione (response vector) è combinazione lineare dei pesi imparati con le feature di un data element

un buon regressore impara dei pesi tali che l'errore di ogni predizione è minimizzato

- con un approccio del tipo Ordinary Least Squares
- magari anche applicando regularization alla funzione obiettivo

## quality of the fitting

la misura che utilizziamo è il coefficient of determination R^2

- it compares the fit of the chosen model with that of a horizontal straight line
- with perfect fitting the numerator of the second term is zero and R^2 = 1
- if the model does not follow the trend of the data the numerator of the second term can reach or exceed the denominator, and R^2 can also be negative

we want to have a number that isn't influenced by the dimension of the data

- MSE e RMSE sono influenzati dalla dimensione dei dati

if we consider only the sum of squared residuals we have

- a big value if the values are big
- a small value if the values are small

## RMSE vs R^2

# Polynomial regression

what if we have a non linear relationship?

we want to use linear methods because other ones are computationally expensive

## Univariate polynomial regression

we can transform the univariate problem to have more variables, with those variables being the powers x^2, x^3, ...

then we can do linear regression

there is a substantial difference between this "synthetic" multivariate linear regression and the real one

- here we have an hyperparameter: the degree of the polynomial
- we can use gridsearch and crossvalidation to choose the degree that best fits the data
  - too low of a degree and we underfit
  - too high of a degree and we overfit

## Polynomial Regression Multivariata

```chatgpt
**la polynomial regression si può fare anche nel caso multivariato**, non è limitata al caso monovariato.

Se hai più variabili indipendenti (x_1, x_2, ..., x_n), puoi comunque costruire un modello polinomiale aggiungendo:

* potenze delle singole variabili: x_1^2; x_2^3; ...

* termini di interazione x_1*x_2, x_1^2*x_3, ...

Ad esempio, con due variabili (x_1, x_2) e polinomio di grado 2:

y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1^2 + \beta_4 x_2^2 + \beta_5 x_1 x_2 + \epsilon

### Come si implementa

L’idea è sempre la stessa: trasformi le feature tramite espansione polinomiale e poi applichi una **regressione lineare** sulle feature espanse.

In Python (scikit-learn):

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

model = Pipeline([
    ("poly", PolynomialFeatures(degree=2)),
    ("lin", LinearRegression())
])

model.fit(X, y)


Dove `X` può avere qualunque numero di colonne.

###  Attenzione però

* Il numero di feature cresce rapidamente con il grado del polinomio (combinatorial explosion).
* Aumenta facilmente l’overfitting → spesso utile usare **regularization (Ridge/Lasso)**.
```

# Overfitting and regularisation

Regularisation is a technique that reduces overfitting. A general way for controlling overfitting is to simplify the model. Regularisation does indeed simplify the model

To simplify a linear multivariete polynomial, we define a loss function dependent on the parameters of the model (weights)

- then we can optimise the weights with gradient descent

## OLS

Ordinary Least Squares (OLS) regression minimizes the prediction error on the training set

**Risk: overfitting, especially with many variables or noisy data**

Regularization: technique to penalize model complexity a way to reduce the complexity is to reduce, in several ways, the values of the coefficients

Goal: find a good trade-off between accuracy and model simplicity

## Lasso regression

L1-norm

- norm of degree 1

this basically does feature selection

L1-regularization encourages sparsity in w

Struggles with collinearity among features

## Ridge regression

we still add a penalty term. A different one

L2-norm

- norm of degree 2 (la norma è la square root of the sum of squares)

dal grafico si vede bene che qua non stiamo facendo feature selection. piuttosto stiamo calibrando i pesi in maniera tale da ridurre overfitting

Al contrario di Lasso, Ridge regressor è adatto in casi in cui si ha: Multicollinear data where features are highly correlated

### Che cosa sono Bias e Variance in un modello di regressione?

```chatgpt
## 🎯 **Bias**

Il *bias* è l’errore introdotto dal fatto che il modello è troppo semplice o troppo rigido per catturare la reale relazione nei dati.

* Un modello **ad alto bias** fa assunzioni forti (es. preferisce pesi molto piccoli → modelli “piatti” o poco flessibili).
* Risultato: **underfitting**
  → il modello non si adatta bene né ai dati di training né ai dati nuovi.

Nel caso della *ridge regression*, un α (lambda) grande spinge i pesi verso zero:
il modello diventa meno flessibile → **bias aumenta**.

---

## 🎯 **Variance**

La *variance* è quanto il modello è sensibile ai cambiamenti nei dati di training.

* Un modello **ad alta varianza** cambia molto se cambiano leggermente i dati.
* Tipico di modelli molto flessibili, che si adattano troppo al training set.
* Risultato: **overfitting**
  → ottimo fit sui dati di training, scarso sui dati nuovi.

Nel caso della ridge:

* un α piccolo ≈ OLS → il modello può avere pesi grandi → è molto flessibile → **alta varianza**.

---

# 📌 Quindi: la varianza di cosa?

👉 **parliamo della varianza delle predizioni del modello** se il modello fosse allenato su diversi dataset simili tra loro.

Immagina di avere 100 campioni di training leggermente diversi (come se facessi bootstrap).
Un modello ad alta varianza:

* cambierebbe molto i suoi parametri,
* produrrebbe predizioni molto diverse fra loro.

Un modello a bassa varianza:

* produrrebbe predizioni simili,
* è più “stabile”.

---

# 📌 Perché succede con Ridge?

| α (lambda) | Effetto                                              | Bias         | Variance     |
| ---------- | ---------------------------------------------------- | ------------ | ------------ |
| **alto**   | forte penalizzazione → pesi piccoli → modello rigido | ↑ aumenta    | ↓ diminuisce |
| **basso**  | penalizzazione debole → pesi liberi                  | ↓ diminuisce | ↑ aumenta    |

---

# 🔎 Riassunto intuitivo

* **Bias = quanto il modello sbaglia perché è troppo semplice.**
* **Variance = quanto le sue predizioni cambiano se cambia leggermente il dataset.**

La ridge “stringe” i coefficienti → riduce flessibilità → riduce varianza → ma introduce bias.
```

## Elastic net regression

Addresses limitations of Ridge and Lasso:

- Ridge cannot perform feature selection
- Lasso struggles when features are highly correlated

Offers a balance between these methods

combines the two penalties

# Comparison of regularized regression techniques

Choosing the right method depends on:

- Presence of multicollinearity
- Sparsity of the solution required (quanta feature selection è necessaria?)
- Dimensionality of the dataset

Elastic net sembra essere OP

## What is the relationship between loss and accuracy?
