def mallow(y, y_pred, y_sub, k, p):
    """
    Return an mallows Cp score for a model.

    Input:
    y: array-like of shape = (n_samples) including values of observed y
    y_pred: vector including values of predicted y
    k: int number of predictive variable(s) used in the model
    p: int number of predictive variable(s) used in the sub model

    Raise Error if p is less than k.
    Raise Error if y , y_sub and y_pred are not in same length.
    Raise Error if length(y) <= 1, length(y_sub)<=1, or length(y_pred) <= 1.
    Raise TypeError if y , y_sub and y_pred are not vector.
    Raise TypeError if p is not int.
    Raise Error if p < 0.
    Raise TypeError if k is not int.
    Raise Error if k < 0.
    """
# what kink of error should i raise???
    import numpy as np
    if len(y)!=len(y_sub) or len(y_sub)!=len(y_pred) or len(y)!= len(y_pred):
        raise Error("The length of observed y, predicted y, and predicted y in subset model must be same")

    if len(y)<=1 or len(y_sub)<=1 or len(y)<=1:
        raise Error("The length of observed y, predicted y, and predicted y in subset model must be larger than 1")

    if (isinstance(y,list)!=True and isinstance(y,numpy.ndarray)) or isinstance(y_sub,list)!=True or isinstance(y_pred,list)!=True:
        raise  TypeError("The observed y, predicted y, and predicted y in subset model must be list ")

    if isinstance(p,int) !=True or isinstance(k,int)!=True:
        raise TypeError("The number of predictive variable(s) used in the sub model must be integer")

    if p<0 or k<0:
        raise TypeError("The number of predictive variable(s) used in the sub model must be positive")

##typo of y should be list or numpy.ndarray(y=np.array([1,2,3,4,]))
    if isinstance(y,list)==True:
        y=np.array(y)
        return y
    if isinstance(y_sub,list)==True:
        y_sub=np.array(y_sub)
        return y_sub
    if isinstance(y_pred,list)==True:
        y_pred=np.array(y_pred)
        return y_pred
    SSE_p=np.sum((y-y_sub)**2)
    MSE= np.mean((y-y_pred)**2)/(len(y)-p)
    mallow=SSE_p/MSE-len(y)+2*p
    return mallow
