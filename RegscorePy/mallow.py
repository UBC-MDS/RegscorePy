def mallow(y, y_pred, y_sub, k, p):
    """
    Return an mallows Cp score for a model.

    Input:
    y: array-like of shape = (n_samples) including values of observed y
    y_pred: vector including values of predicted y
    k: int number of predictive variable(s) used in the model
    p: int number of predictive variable(s) used in the sub model

    Raise Error if k is less than p.
    Raise Error if y , y_sub and y_pred are not in same length.
    Raise Error if length(y) <= 1, length(y_sub)<=1, or length(y_pred) <= 1.
    Raise TypeError if y , y_sub and y_pred are not vector.
    Raise TypeError if p is not int.
    Raise Error if p < 0.
    Raise TypeError if k is not int.
    Raise Error if k < 0.
    """

    import numpy as np

    if k<p:
        raise Exception("number of predictive variable(s) used in the model must larger than in subset model")
    if len(y)!=len(y_sub) or len(y_sub)!=len(y_pred) or len(y)!= len(y_pred):
        raise Exception("The length of observed y, predicted y, and predicted y in subset model must be same")

    if len(y)<=1 or len(y_sub)<=1 or len(y)<=1:
        raise Exception("The length of observed y, predicted y, and predicted y in subset model must be larger than 1")

    if (isinstance(y,list)!=True and isinstance(y,numpy.ndarray)!=True) or (isinstance(y_sub,list)!=True and isinstance(y_sub,numpy.ndarray)!=True) or (isinstance(y_pred,list)!=True and isinstance(y_pred,numpy.ndarray)!=True):
        raise  TypeError("The observed y, predicted y, and predicted y in subset model must be list ")

    if isinstance(p,int) !=True or isinstance(k,int)!=True:
        raise TypeError("The number of predictive variable(s) used in the sub model must be integer")

    if p<0 or k<0:
        raise TypeError("The number of predictive variable(s) used in the sub model must be positive")



    if isinstance(y,list)==True:
        y=np.array(y)

    if isinstance(y_sub,list)==True:
        y_sub=np.array(y_sub)

    if isinstance(y_pred,list)==True:
        y_pred=np.array(y_pred)

    SSE_p=np.sum((y-y_sub)**2)
    MSE= np.sum((y-y_pred)**2)/(len(y)-k)
    mallow=SSE_p/MSE-len(y)+2*p
    return mallow
