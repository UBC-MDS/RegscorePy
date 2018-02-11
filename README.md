# regscore-py

A python package that does model comparison between different regression models.

A project by:
- Ha Dinh
- Simran Sethi
- Ruoqi Xu

## **Overview**

### Problem

Currently, in both Python and R ecosystems, there is no single package that provides easy calculation for AIC, BIC, Mallow's $C_p$, and a united table summary of scores for all models that users can refer to to compare and choose the best model. This leads to manual mathematical calculation, lengthy codes or usage of several packages to obtain one task, which is inefficient.

### Solution

Acknowledging this problem, we want to build a united package which provides users instant computation for various model comparison metrics such as:

- Mean Square error
- Root mean square error
- Mean absolute error
- Mean Percentage error
- Mean absolute percentage error
- AIC
- BIC
- Mallow's $C_p$

In addition to all model comparison score functions, we want to have a function to output a summary table that combines scores for all models users want to compare. This table helps users avoid scrolling through lines of output or call score outputs with additional code to get all scores. This table of comparison is not recommended to be used if users want to compare models with different methods (e.g. linear regression, logistic regression, GLM)

### How solution fits to Python ecosystem

Python's machine learning package Scikit-learn has some functions to calculate regression metrics, including:

```
metrics.explained_variance_score(y_true, y_pred)

metrics.mean_absolute_error(y_true, y_pred)

metrics.mean_squared_error(y_true, y_pred[, …])

metrics.mean_squared_log_error(y_true, y_pred)

metrics.median_absolute_error(y_true, y_pred)

metrics.r2_score(y_true, y_pred[, …])
```

However, there are no functions for AIC, BIC, Mallow's $C_p$ and table output. Thus, our package can be a united source for all popular regression model comparison metrics.

## **Timeline**

**Phase I**: 02/05/2018 - 03/11/2018, develop functions to compute AIC, BIC, Mallow's $C_p$ and table output that include all scores for model comparison.
- ** **Phase II**: From late March, develop other functions to finish the package.

* ** Tentative, and will be updated later

## **Function Description**

Here, we will describe functions in *Phase I*. We will also add a documentation for all functions later.

### AIC

#### Introduction

AIC stands for Akaike’s Information Criterion. It estimates the quality of a model, relative to each of other models. The lower AIC score is, the better the model is. Therefore, a model with lowest AIC - in comparison to others, is chosen.

```
AIC = n*log(residual sum of squares/n) + 2K
```

where:
- n: number of observations
- K: number of parameters (including intercept)

#### Function

```
aic(x, y, n, k, model = 'linear')
```

**Parameters:**
* **x**: ndarray or scipy.sparse matrix, (n_samples, n_features)
  * Predictive variable(s)

* **y**: ndarray, shape (n_samples), or (n_samples, n_targets)
  * Target variable(s)

* **n**: int
  * Number of observations

* **k**: int
  * Number of predictive variable(s) used in the model

* **model**: default 'linear' | 'logistic' | 'ridge' | 'lasso' | 'elasticnet'
  * Method applied to the model

**Return:**
* AIC score of the model: int


### BIC

#### Introduction

BIC stands for Bayesian Information Criterion. Like AIC, it also estimates the quality of a model. When fitting models, it is possible to increase model fitness by adding more parameters. Doing this may results in model overfit. Both AIC and BIC helps to resolve this problem by using a penalty term for the number of parameters in the model. This term is bigger in BIC than in AIC.

```
BIC = n*log(residual sum of squares/n) + K*log(n)
```

where:
- n: number of observations
- K: number of parameters (including intercept)

#### Function

```
bic(x, y, n, k, model = 'linear')
```
**Parameters:**
* **x**: ndarray or scipy.sparse matrix, (n_samples, n_features)
  * Predictive variable(s)

* **y**: ndarray, shape (n_samples), or (n_samples, n_targets)
  * Target variable(s)

* **n**: int
  * Number of observations

* **k**: int
  * Number of predictive variable(s) used in the model

* **model**: default 'linear' | 'logistic' | 'ridge' | 'lasso' | 'elasticnet'
  * Method applied to the model

**Return:**
* BIC score of the model: int

### Mallow's C_p

#### Introduction

Mallow's C_p is named for Colin Lingwood Mallows. It is used to assess the fit of regression model, finding the best model involving a subset of predictive variables available for predicting some outcome. 

```
C_p = (SSE_p/MSE) - (n - 2p)
```

where:
- SSE_k: residual sum of squares for the subset model containing `p` explanatory
variables counting the intercept.
- MSE: mean squared error for the full model (model containing all `k` explanatory variables of interest)
- n: number of observations
- p: number of subset explanatory variables

#### Function

```
mallow(X, x_subset, y, n, p, k, model = 'linear')
```

**Parameters:**
* **X**: ndarray or scipy.sparse matrix, (n_samples, n_features)
  * Predictive variable(s)

* **x_subset**: ndarray or scipy.sparse matrix, (n_samples, n_features)
  * Predictive variable(s) in the subset model

* **y**: ndarray, shape (n_samples), or (n_samples, n_targets)
  * Target variable(s)

* **n**: int
  * Number of observations

* **p**: int
  * Number of predictive variable(s) used in the subset model

* **k**: int
  * Number of predictive variable(s) used in the model

* **model**: default 'linear' | 'logistic' | 'ridge' | 'lasso' | 'elasticnet'
  * Method applied to the model

**Return:**
* Mallow's C_p score of the subset model: int


### Table of comparison

#### Function

```
comparison_model(model)
```

**Parameters:**
* **model**: str
  * Models to compare, separate by `,`

**Return:**
* A table with model names and their scores. Demo:

| Model  | AIC | BIC | Mallow's C_p |
|--------|-----|-----|--------------|
| Model1 | 123 | 145 | 156          |
| Model2 | 145 | 134 | 167          |
