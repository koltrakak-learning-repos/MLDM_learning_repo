in regression the target is numeric

# quality of the fitting

we want to have a number that isn't influenced by the dimension of the data

if we consider only the sum of squared residuals we have

- a big value if the values are big
- a small value if the values are small

# Polynomial regression

what if we have a non linear relationship?

we want to use linear methods because other ones are computationally expensive

we can transform the univariate problem to have more variables, with those variables being the powers x^2, x^3, ...

then we can do linear regression

there is a substantial difference between this "synthetic" multivariate linear regression and the real one

- here we have an hyperparameter: the degree of the polynomial
- we can use gridsearch to choose the degree that best fits the data
  - to low of a degree and we underfit
  - to high of a degree and we overfit

# Overfitting and regularisation

regularisation is a technique that reduces overfitting

we define a loss function dependent on the parameters of the model (weights in linear regression)

- we can optimise the weights with gradient descent

## Lasso regression

L1-norm

- norm of degree 1

this basically does feature selection

## Ridge regression

we still add a penalty term. A different one

L2-norm

- norm of degree 2 (la norma è la square root of the sum of squares)

dal grafico si vede bene che qua non stiamo facendo feature selection. piuttosto stiamo calibrando i pesi in maniera tale da ridurre overfitting

## Elastic net regression

combines the two penalties

## What is the relationship between loss and accuracy?
