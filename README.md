# model-comparison-package
This is the repo for a python package that does model comparison between different feature selection models.

Name of contributors:
Ha Dinh
Simran Sethi
Ruoqi Xu


High-level description:
Problem faced: no united package to compute AIC, BIC and Mallow’s C_p in both R and Python environment → manual, lengthy code → inefficient!
      - What do we propose to solve it: a package that produces AIC, BIC, Mallow’s C_p and a table that combine model’s scores for easy comparison.
      - How is this package better/different than others in the market:


All the regression model selection package functions:
Description for each function
AIC:
BIC
Mallow’s C_p
Add-on Output of function: Table that combines scores of all models for easy comparison

How this package fits into:
Python ecosystem:
Scikit-learn has some, but not what we offer
           http://scikit-learn.org/stable/modules/classes.html#module-sklearn.linear_model
R ecosystem:
`finish_glance`  function from broom package
    https://www.rdocumentation.org/packages/broom/versions/0.4.2/topics/finish_glance
