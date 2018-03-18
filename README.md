
# RegscorePy

[![Build Status](https://travis-ci.org/UBC-MDS/RegscorePy.svg?branch=master)](https://travis-ci.org/UBC-MDS/RegscorePy) [![codecov](https://codecov.io/gh/UBC-MDS/RegscorePy/branch/master/graphs/badge.svg)](https://codecov.io/gh/UBC-MDS/RegscorePy)


A python package that does model comparison between different regression models.

## Installation

```bash
pip install git+https://github.com/UBC-MDS/RegscorePy.git
```


## **Function Description And Usage**


### AIC

AIC stands for Akaike’s Information Criterion. It estimates the quality of a model, relative to each of other models. The lower AIC score is, the better the model is. Therefore, a model with lowest AIC - in comparison to others, is chosen.

```
AIC = n*log(residual sum of squares/n) + 2K
```

where:
- n: number of observations
- K: number of parameters (including intercept)

#### Function

```
aic(y, y_pred, p)
```

**Parameters:**

* **y**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * True target variable(s)

* **y_pred**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * Fitted target variable(s) obtained from your regression model

* **p**: int
  * Number of predictive variable(s) used in the model

**Return:**
* aic_score: int
  * AIC score of the model


### BIC

BIC stands for Bayesian Information Criterion. Like AIC, it also estimates the quality of a model. When fitting models, it is possible to increase model fitness by adding more parameters. Doing this may result in model overfit. Both AIC and BIC help to resolve this problem by using a penalty term for the number of parameters in the model. This term is bigger in BIC than in AIC.

```
BIC = n*log(residual sum of squares/n) + K*log(n)
```

where:
- n: number of observations
- K: number of parameters (including intercept)

#### Function

```
bic(y, y_pred, p)
```
**Parameters:**
* **y**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * True target variable(s)

* **y_pred**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * Fitted target variable(s) obtained from your regression model

* **p**: int
  * Number of predictive variable(s) used in the model

**Return:**
* bic_score: int
  * BIC score of the model


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
mallow(y, y_pred, y_sub, k, p)
```

**Parameters:**

* **y**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * True target variable(s)

* **y_pred**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * Fitted target variable(s) obtained from your regression model

* **y_sub**: array-like of shape = (n_samples) or (n_samples, n_outputs)
  * Fitted target variable(s) obtained from your subset regression model

* **k**: int
  * Number of predictive variable(s) used in the model

* **p**: int
  * Number of predictive variable(s) used in the subset model

**Return:**

* mallow_score: int
  * Mallow's C_p score of the subset model


## Usage

```
>> from RegscorePy import *
>> y = [1,2,3,4]
>> y_pred = [5,6,7,8]
>> p = 3
>> aic.aic(y, y_pred, p)
17.090354888959126
>>
>>
>> bic.bic(y, y_pred, p)
15.249237972318795
>>
>>
>> y_sub = [1,2,3,5]
>> k = 3
>> p = 2
>> mallow.mallow(y, y_pred, y_sub, k, p) 
>> 0.015625

```

* This usage apply to python3. If you use python2, please run `from __future__ import division` before run the function.


## How to run tests

From root directory, run all test files in terminal:

```
python -m pytest
```

You also have the option to run individual test files by referencing its path. For example, if you want to test aic function, you can use the command below: 

```
python -m pytest RegscorePy/test/test_aic.py
```

## License
[MIT](LICENSE)

## Contributing
This is an open source project. Please follow the guidelines below for contribution.
  - Open an issue for any feedback and suggestions.
  - For contributing to the project, please refer to [Contributing](CONTRIBUTING.md) for details.
