def aic(y, y_pred, p):
    """
    Return an AIC score for a model.

    Input:
    y: array-like of shape = (n_samples) including values of observed y
    y_pred: vector including values of predicted y
    p: int number of predictive variable(s) used in the model

    Output:
    aic_score: int or float AIC score of the model

    Raise TypeError if y or y_pred are not list/tuple/dataframe column/array.
    Raise TypeError if elements in y or y_pred are not integer or float.
    Raise TypeError if p is not int.
    Raise InputError if y or y_pred are not in same length.
    Raise InputError if length(y) <= 1 or length(y_pred) <= 1.
    Raise InputError if p < 0.
    """

    # Package dependencies
    import numpy as np
    import pandas as pd

    # User-defined exceptions
    class InputError(Exception):
        """
        Raised when there is any error from inputs that no base Python exceptions cover.
        """
        pass

    # Check conditions:
    ## Type condition 1: y and y_pred should be array-like containing numbers
    ### check type of y and y_pred
    if isinstance(y, (np.ndarray, list, tuple, pd.core.series.Series)) == False or isinstance(y_pred, (np.ndarray, list, tuple, pd.core.series.Series)) == False:
        raise TypeError("Expect array-like shape (e.g. array, list, tuple, data column)")
    ### check if elements of y and y_pred are numeric
    else:
        for i in y:
            for j in y_pred:
                if isinstance(i, (int, float)) != True or isinstance(j, (int, float)) != True:
                    raise TypeError("Expect numeric elements in y and y_pred")

    ## Type condition 2: p should be positive integer
    ### check if p is integer
    if isinstance(p, int) != True:
        raise TypeError("Expect positive integer")
    ### check if p is positive
    elif p <= 0:
        raise InputError("Expect positive integer")

    ## Length condition: length of y and y_pred should be equal, and should be more than 1
    ### check if y and y_pred have equal length
    if not len(y) == len(y_pred):
        raise InputError("Expect equal length of y and y_pred")
    ### check if y and y_pred length is larger than 1
    elif len(y) <= 1 or len(y_pred) <= 1:
        raise InputError("Expect length of y and y_pred to be larger than 1")
    else:
        n = len(y)

    # Calculation
    resid = np.subtract(y_pred, y)
    rss = np.sum(np.power(resid, 2))
    aic_score = n*np.log(rss/n) + 2*p

    return aic_score
