In regression the target is numeric; the goal is forecasting continuous values

response vector == predizione (vettore colonna, una predizione per ogni riga del dataset)

# Linear regression

modelliamo la relazione tra attributi e variabile dipendente come una **combinazione lineare degli attributi**

- per l'i-esima riga: y_i = w^T * x_i
- definisco un iperpiano nello spazio d-dimensionale; con d numero di attributi

i pesi che impariamo sono numerosi tanto quanto il numero di feature del dataset

la predizione (response vector) è combinazione lineare dei pesi imparati con le feature di un data element

un buon regressore impara dei pesi tali che l'errore di ogni predizione rispetto alla label target è minimizzato across the training set

- con un approccio del tipo Ordinary Least Squares
- magari anche applicando regularization alla funzione obiettivo

## quality of the fitting

Possiamo utilizzare MSE o RMSE, ma abbiamo un problema

- MSE e RMSE sono influenzati dalla dimensione dei dati
  - consider the sum of squared residuals we have
    - a big value if the values are big
    - a small value if the values are small

we want to have a number that isn't influenced by the dimension of the data, in questo modo possiamo capire più facilmente la qualità del fitting

- se è vicino a 1 è buono

la misura che utilizziamo a questo scopo è il **coefficient of determination R^2**: 1 - SSE/SST

- it compares the fit of the chosen model with that of a horizontal straight line
- with perfect fitting the numerator of the second term is zero and R^2 = 1
- if the model does not follow the trend of the data the numerator of the second term can reach or exceed the denominator
  - R^2 comincia a diventare minore di uno
  - R^2 can also be negative

# Polynomial regression

what if we have a non linear relationship between the predictor variables and the target?

we want to use linear methods because other ones are computationally expensive

## Univariate polynomial regression

un problema univariato è un problema in cui ho solo una variabile predictor

se la relazione tra il predictor è il mio target non è lineare, we can transform the univariate problem to have more variables, with those variables being the powers of the predictor: x^2, x^3, ...

then we can do linear regression

**NB**: questo è un esempio di feature transformation/engineering, stiamo ottenendo altri attributi trasformando quello che abbiamo già

**NB**: there is a substantial difference between this "synthetic" multivariate linear regression and the real one

- here we have an hyperparameter: the degree of the polynomial
- we can use gridsearch and crossvalidation to choose the degree that best fits the data looking at RMSE or R^2
  - too low of a degree and we underfit the training data
  - too high of a degree and we overfit, we learn the noise of the training data

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

# Fitting, overfitting and regularisation

The standard multivariate linear regression does not have hyperparameters for controlling the fitting quality, in particular to guarantee good performance on the test set

- corriamo il rischio di overfittare il training set se non facciamo nulla

Regularisation is a technique that reduces overfitting.

- A general way for controlling overfitting is to simplify the model.
- Regularisation does indeed simplify the model

To simplify a linear multivariate polynomial, we define a loss function dependent on the parameters of the model (weights)

- tipicamente la loss function è MSE

## OLS

Ordinary Least Squares (OLS) regression minimizes the prediction error (loss) on the training set

- ammette un metodo esatto (formula chiusa) ma tipicamente si utilizza discesa del gradiente per approssimare i pesi ottimi
  - il metodo esatto non scala per dataset grandi

**Risk: overfitting, especially with many variables or noisy data**

Applichiamo quindi regularization techniques to penalize model complexity and reduce overfitting

- modelli complessi generalizzano male se il problema non ha qullo stesso grado di complessità (apprendono rumore)
- a way to reduce the complexity is to reduce, in several ways, the values of the coefficients

Goal: find a good trade-off between accuracy on the training set and model simplicity

- chiaramente se regolarizzo troppo vado in underfitting

## Lasso regression

Aggiungo la L1-norm dei pesi (norm of degree 1) alla loss

- sommatoria del valore assoluto dei pesi
- questa è pesata da un ipeparametro alpha che definisce quanta regularization stiamo applicando

Penalizza pesi grandi

- encourages sparsity in W
- **this basically does feature selection**

NB: con lasso regression, alla fine del training, w embodies the importance of each feature in the regression model

- questo perchè solamente le feature importanti (quelle che riducono tanto la loss) hanno il privilegio di avere un peso grande
- le feature meno importanti avranno il loro peso ridotto dalla lasso penalty
  - come è giusto che sia, feature poco importanti sono solo causa di overfitting

struggles when predicting features are highly correlated

- Tends to choose one arbitrarily instead of taking them together
- se una è importante, anche l'altra è importante (?) e lasso ne scarta via una

## Ridge regression

we still add a penalty term. A different one L2-norm

- norm of degree 2 (la norma è la square root of the sum of squares)
- di nuovo penalizziamo pesi grandi

dal grafico si vede bene che qua non stiamo facendo feature selection.

- Piuttosto stiamo calibrando i pesi in maniera tale da ridurre overfitting

Al contrario di Lasso, Ridge regression è adatto in casi in cui si ha multicollinear data (predicting features are highly correlated)

- Tends to select them together rather than choosing one arbitrarily, shrinks their coefficients toward each other using the Ridge-like penalty
- questo non è un problema dal punto di vista della predizione dato che, come abbiamo visto, feature altamente correlate tra di loro sono ridondanti
- è un problema dal punto di vista dell'interpratabilità del modello dato che sembra che la feature scartata non sia importante

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

- combines the two penalties

Elastic net sembra essere OP ma richiede il tuning di due iperparametri

# Comparison of regularized regression techniques

Choosing the right method depends on:

- Presence of multicollinearity
- Sparsity of the solution required (quanta feature selection è necessaria?)
- Dimensionality of the dataset
