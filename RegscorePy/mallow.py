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
