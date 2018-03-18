import os
import sys
import pytest

sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../"))

from RegscorePy.bic import bic



# test all BIC functions
class Test_bic:

    def test_type_y_ypred(self):
        """
        Raise TypeError if y and y_pred are not vector.
        """
        with pytest.raises(TypeError):
            bic("a", [[1, 2], [2, 2]], 3.3)

    def test_type_y_ypred2(self):
        """
        Raise TypeError if elements of y or y_pred are not integers.
        """
        with pytest.raises(TypeError):
            bic("c", [1, 2], 3.4)

    def test_type_y_ypred3(self):
        """
        Raise TypeError if elements of y or y_pred are not integers.
        """
        with pytest.raises(TypeError):
            bic(complex(3,4), [1, 2], 3.4)

    def test_type_y_ypred4(self):
        """
        Raise TypeError if elements of y or y_pred are not integers.
        """
        with pytest.raises(TypeError):
            bic([1, 2], complex(3,4), 3.4)

    def test_len_y_ypred(self):
        """
        Raise Error if elements of y or y_pred are not same lengths.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [1, 2], 3)


    def test_len_y_ypred2(self):
        """
        Raise Error if elements of y or y_pred are not same lengths.
        """
        with pytest.raises(TypeError):
            bic([1, 2], [1, 2, 3, 4], 3)

    def test_len_y_elements(self):
        """
        Raise Error if elements of y or y_pred are not same lengths.
        """
        with pytest.raises(TypeError):
            bic([1, 2, complex(1,2), 5], [1, 2, 3, 4], 3)

    def test_len_ypred_elements(self):
        """
        Raise Error if elements of y or y_pred are not same lengths.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 5], [1, 2, complex(1,2), 4], 3)


    def test_len_grt1(self):
        """
        Raise Error if y or y_pred less than 1
        """
        with pytest.raises(TypeError):
            bic([], [1, 2, 3, 4], 3)

    def test_len_grt1_2(self):
        """
        Raise Error if elements of y or y_pred are not same lengths.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [], 3)

    def test_p(self):
        """
        Raise TypeError if p is not an integer.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], "c")

    def test_p2(self):
        """
        Raise TypeError if p is not greater than 0
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], -1)

    def test_p3(self):
        """
        Raise TypeError if p is not integer
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], 2.86)

    def test_p4(self):
        """
        Raise TypeError if p is greater than 0, if nor raise error.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], 0)

    def test_p5(self):
        """
        Raise TypeError if p is integer if nor raise typeerror.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], [12, 3])

    def test_p6(self):
        """
        Raise TypeError if p is integer if nor raise typeerror.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], complex(1,2))


    def test_type_y_ypred3(self):
        """
        Raise TypeError if y or y_pred are matrices.
        """
        with pytest.raises(TypeError):
            bic([[1, 2, 3, 4],
                            [5, 6, 6, 7]], [1, 2, 3, 4], 3)

    def test_input(self):
        """
        check if input are more than the required, raise error if so.
        """
        with pytest.raises(TypeError):
            bic([1], [3], [2], 3, 2)

    def test_exp_result1(self):
        """
        test if aic() gives correct result
        """
        y = [1, 2, 3, 4]
        y_pred = [5, 6, 7, 8]
        p = 3
        ob = round(bic(y, y_pred, p), 3)
        exp = 15.249
        assert ob == exp, 'The AIC given y = [1,2,3,4], y_pred = [5,6,7,8], and p = 3 should be 15.249 (applying statistical formula in main README, and rounded to 3 decimals)'

