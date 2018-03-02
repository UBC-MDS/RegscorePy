def aic(y, y_pred, p):
    """
    Return an AIC score for a model.
    Input:
    y: array-like of shape = (n_samples) including values of observed y
    y_pred: vector including values of predicted y
    p: int number of predictive variable(s) used in the model

    Raise Error if y and y_pred are not in same length.
    Raise Error if length(y) <= 1 or length(y_pred) <= 1.
    Raise TypeError if y and y_pred are not vector.
    Raise TypeError if p is not int.
    Raise Error if p < 0.
    """
