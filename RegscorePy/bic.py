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