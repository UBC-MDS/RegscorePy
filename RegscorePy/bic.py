def bic(y, y_pred, p):
    """
    Returns the BIC score of a model.

    Input:-
    y: the labelled data in shape of an array of size  = number of samples. 
        type = vector/array/list
    y_pred: predicted values of y from a regression model in shape of an array
        type = vector/array/list
    p: number of variables used for prediction in the model.
        type = int

    Output:-
    score: It outputs the BIC score
        type = int


    Tests:-
    Raise Error if length(y) <= 1 or length(y_pred) <= 1.
    Raise Error if length(y) != length(y_pred).
    Raise TypeError if y and y_pred are not vector.
    Raise TypeError if elements of y or y_pred are not integers.
    Raise TypeError if p is not an int.
    Raise Error if p < 0.
    """

    # package dependencies
    import numpy as np
    import pandas as pd
    import collections

    # Input type error exceptions
    if not isinstance(y, (collections.Sequence, np.ndarray, pd.core.series.Series)):
        raise TypeError("Argument 1 not like an array.")

    if not isinstance(y_pred, (collections.Sequence, np.ndarray, pd.core.series.Series)):
        raise TypeError("Argument 2 not like an array.")

    for i in y:
        if not isinstance(i, (int, float)):
            raise TypeError("All elements of argument 1 must be int or float.")

    for i in y_pred:
        if not isinstance(i, (int, float)):
            raise TypeError("All elements of argument 2 must be int or float.")

    if not isinstance(p, (int, float)):
        raise TypeError("'Number of variables' must be of type int or float.")

    if p <= 0:
        raise TypeError("'Number of variables' must be positive integer.")

    if isinstance(p, int) != True:
        raise TypeError("Expect positive integer")

    if len(y) <= 1 or len(y_pred) <= 1:
        raise TypeError("observed and predicted values must be greater than 1")

    # Length exception
    if not len(y) == len(y_pred):
        raise TypeError("Equal length of observed and predicted values expected.")
    else:
        n = len(y)

    # Score

    residual = np.subtract(y_pred, y)
    SSE = np.sum(np.power(residual, 2))
    BIC = n*np.log(SSE/n) + p*np.log(n)
    return BIC
