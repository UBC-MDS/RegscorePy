def mallow(y, y_pred, y_sub, k, p):
    """
    Return an mallows Cp score for a model.

    Input:
    y: array-like of shape = (n_samples) including values of observed y
    y_pred: vector including values of predicted y
    k: int number of predictive variable(s) used in the model
    p: int number of predictive variable(s) used in the sub model

    Output:
    mallow_score: int or float Mallows Cp score of the model and sub model

    Raise InputError if k is less than p.
    Raise InputError if y , y_sub and y_pred are not in same length.
    Raise InputError if length(y) <= 1, length(y_sub)<=1, or length(y_pred) <= 1.
    Raise TypeError if y , y_sub and y_pred are not vector.
    Raise TypeError if p is not int.
    Raise InputError if p < 0.
    Raise TypeError if k is not int.
    Raise InputError if k < 0.
    """

    import numpy as np
    import pandas as pd


    if k<p:
        raise ValueError("number of predictive variable(s) used in the model must larger than in subset model")
    if len(y)!=len(y_sub) or len(y_sub)!=len(y_pred) or len(y)!= len(y_pred):
        raise ValueError("The length of observed y, predicted y, and predicted y in subset model must be same")

    if len(y)<=1 or len(y_sub)<=1 or len(y)<=1:
        raise ValueError("The length of observed y, predicted y, and predicted y in subset model must be larger than 1")

    if isinstance(y, (np.ndarray, list, tuple, pd.core.series.Series)) == False or isinstance(y_pred, (np.ndarray, list, tuple, pd.core.series.Series)) == False:
        raise TypeError("The observed y, predicted y, and predicted y in subset model must be array-like shape (e.g. array, list, tuple, data column)")
    else:
        for i in y:
            for j in y_pred:
                if isinstance(i, (int, float)) != True or isinstance(j, (int, float)) != True:
                    raise TypeError("The observed y, predicted y, and predicted y in subset model must be numeric elements")

    if isinstance(p,int) !=True or isinstance(k,int)!=True:
        raise TypeError("The number of predictive variable(s) used in the sub model must be integer")

    if p<=0 or k<=0:
        raise Exception("The number of predictive variable(s) used in the sub model must be positive")



    if isinstance(y,list)==True:
        y=np.array(y)

    if isinstance(y_sub,list)==True:
        y_sub=np.array(y_sub)

    if isinstance(y_pred,list)==True:
        y_pred=np.array(y_pred)

    SSE_p=np.sum((y-y_sub)**2)
    MSE= np.sum((y-y_pred)**2)/(len(y)-k)
    mallowcp=SSE_p/MSE-len(y)+2*p
    return mallowcp
