import pytest
import RegscorePy

## Add code to test AIC function
class Test_aic:
    ## test function
    def exp_result1():
        """
        test if aic() gives correct result
        """
        y = [1,2,3,4]
        y_pred = [5,6,7,8]
        p = 3
        obs = aic(y, y_pred, p)
        exp = 72
        assert obs == exp, 'The AIC given y = [1,2,3,4], y_pred = [5,6,7,8], and p = 3 should be 72 (applying statistical formula in main README)'


    ## test constrains
    def y_ypred_len():
        """
        test if y and y_pred have same length, if not yield error
        """
        with pytest.raises(Error):
            RegscorePy.aic([1,2,3,4],[4,5,6,7,8], 3)

    def y_len():
        """
        test if length of y is larger than 1, if not yield error
        """
        with pytest.raises(Error):
            RegscorePy.aic([3],[5,6,7,8], 2)

    def ypred_len():
        """
        test if length of y_pred is larger than 1, if not yield error
        """
        with pytest.raises(Error):
            RegscorePy.aic([1,2,3,4],[5], 2)

    def type_p():
        """
        test if p is int, if not yield error
        """
        with pytest.raises(TypeError):
            RegscorePy.aic([1,2,3,4],[5,6,7,8], "a")

    def type_y():
        """
        test if y is a vector or array-like type, if not yield error
        """
        with pytest.raises(TypeError):
            RegscorePy.aic([[1,0,0,0],
                            [0,2,0,0],
                            [0,0,3,0],
                            [0,0,0,4]], [5,6,7,8], 3)

    def type_ypred():
        """
        test if y_pred is a vector or array-like type, if not yield error
        """
        with pytest.raises(TypeError):
            RegscorePy.aic([1,2,3,4], [[5,0,0,0],
                                       [0,6,0,0],
                                       [0,0,7,0],
                                       [0,0,0,8]], 3)

    def value_p():
        """
        test if p is larger than 0, if not yield error
        """
        with pytest.raises(Error):
            RegscorePy.aic([1,2,3,4],[5,6,7,8], -1)
