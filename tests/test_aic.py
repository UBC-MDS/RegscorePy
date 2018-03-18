import os
import sys
import pytest

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

from RegscorePy.aic import aic




class Test_aic():

    # test function
    def test_exp_result1(self):
        """
        test if aic() gives correct result
        """
        y = [1, 2, 3, 4]
        y_pred = [5, 6, 7, 8]
        p = 3
        ob = round(aic(y, y_pred, p), 3)
        exp = 17.09
        assert ob == exp, 'The AIC given y = [1,2,3,4], y_pred = [5,6,7,8], and p = 3 should be 17.09 (applying statistical formula in main README, and rounded to 3 decimals)'

    def test_exp_result2(self):
        """
        test if aic() gives correct result
        """
        y = [-5, 1, -8, -12]
        y_pred = [-4, -6, -8, 1]
        p = 5
        ob = round(aic(y, y_pred, p), 3)
        exp = 26.011
        assert ob == exp, 'The AIC given y = [-5,1,-8,-12], y_pred = [-4,-6,-8,1], and p = 5 should be 26.011 (applying statistical formula in main README, and rounded to 3 decimals)'

    def test_exp_result3(self):
        """
        test if aic() gives correct result
        """
        y = [9.80, 105.23, 4.51, -65.75]
        y_pred = [9.81, 100.10, 4.51, -65.70]
        p = 10
        ob = round(aic(y, y_pred, p), 3)
        exp = 27.536
        assert ob == exp, 'The AIC given y = [9.80, 105.23, 4.51, -65.75], y_pred = [9.81, 100.10, 4.51, -65.70], and p = 10 should be 27.536 (applying statistical formula in main README, and rounded to 3 decimals)'

    def test_exp_result4(self):
        """
        test if aic() gives correct result
        """
        y = [0, 0, 0, -65.789]
        y_pred = [1, 0, 0.9, -64]
        p = 4
        ob = round(aic(y, y_pred, p), 3)
        exp = 8.901
        assert ob == exp, 'The AIC given y = [0, 0, 0, -65.789], y_pred = [1, 0, 0.9, -64], and p = 4 should be 8.901 (applying statistical formula in main README, and rounded to 3 decimals)'

    # test constrains
    # test length of y and y_pred
    def test_y_ypred_len(self):
        """
        test if y and y_pred have same length, if not yield error
        """
        with pytest.raises(Exception):
            aic([1,2,3,4],[4,5,6,7,8], 3)


    def test_y_len1(self):
        """
        test if length of y is larger than 1, if not yield error
        """
        with pytest.raises(Exception):
            aic([3],[5,6,7,8], 2)


    def test_y_len2(self):
        """
        test if length of y is larger than 1, if not yield error
        """

        with pytest.raises(Exception):
            aic([],[5,6,7,8], 2)


    def test_ypred_len1(self):
        """
        test if length of y_pred is larger than 1, if not yield error
        """
        with pytest.raises(Exception):
            aic([1, 2, 3, 4], [5], 2)


    def test_ypred_len2(self):
        """
        test if length of y_pred is larger than 1, if not yield error
        """
        with pytest.raises(Exception):
            aic([1, 2, 3, 4], [], 2)


    # test type of y and y_pred
    def test_type_y1(self):
        """
        test if y is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic([[1, 0, 0, 0],
                            [0, 2, 0, 0],
                            [0, 0, 3, 0],
                            [0, 0, 0, 4]], [5, 6, 7, 8], 3)

    def test_type_y2(self):
        """
        test if y is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic(5, [5, 6, 7, 8], 3)

    def test_type_y3(self):
        """
        test if y is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic(["a", "b", "c", "d"], [5, 6, 7, 8], 3)

    def test_type_y4(self):
        """
        test if y is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic("a", [5, 6, 7, 8], 3)

    def test_type_ypred1(self):
        """
        test if y_pred is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic([1, 2, 3, 4], [[5, 0, 0, 0],
                                          [0, 6, 0, 0],
                                          [0, 0, 7, 0],
                                          [0, 0, 0, 8]], 3)

    def test_type_ypred2(self):
        """
        test if y_pred is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic([1, 2, 3, 4], 5, 3)

    def test_type_ypred3(self):
        """
        test if y_pred is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic([5, 6, 7, 8], ["a", "b", "c", "d"], 3)

    def test_type_ypred4(self):
        """
        test if y_pred is a vector or array-like type including numbers, if not yield error
        """
        with pytest.raises(TypeError):
            aic([5, 6, 7, 8], "a", 3)

    # test type of p
    def test_type_p1(self):
        """
        test if p is int, if not yield error
        """
        with pytest.raises(TypeError):
            aic([1, 2, 3, 4], [5, 6, 7, 8], "a")

    def test_type_p2(self):
        """
        test if p is int, if not yield error
        """
        with pytest.raises(TypeError):
            aic([1, 2, 3, 4], [5, 6, 7, 8], 4.78)

    def test_type_p3(self):
        """
        test if p is int, if not yield error
        """
        with pytest.raises(TypeError):
            aic([1, 2, 3, 4], [5, 6, 7, 8], [3, 0, 0, 0])

    # test value of p
    def test_value_p1(self):
        """
        test if p is larger than 0, if not yield error
        """
        with pytest.raises(Exception):
            aic([1, 2, 3, 4], [5, 6, 7, 8], -1)


    def test_value_p2(self):
        """
        test if p is larger than 0, if not yield error
        """
        with pytest.raises(Exception):
            aic([1, 2, 3, 4], [5, 6, 7, 8], 0)
