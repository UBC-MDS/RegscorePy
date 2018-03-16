import pytest
from RegscorePy import bic


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

    def test_len_grt1(self):
        """
        Raise Error if y or y_pred less than 1
        """
        with pytest.raises(Exception):
            bic([], [1, 2, 3, 4], 3)

    def test_len_grt1_2(self):
        """
        Raise Error if elements of y or y_pred are not same lengths.
        """
        with pytest.raises(Exception):
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
        with pytest.raises(Exception):
            bic([1, 2, 3, 4], [5, 6, 7, 8], -1)

    def test_p3(self):
        """
        Raise TypeError if p is not integer
        """
        with pytest.raises(Exception):
            bic([1, 2, 3, 4], [5, 6, 7, 8], 2.86)

    def test_p4(self):
        """
        Raise TypeError if p is greater than 0, if nor raise error.
        """
        with pytest.raises(Exception):
            bic([1, 2, 3, 4], [5, 6, 7, 8], 0)

    def test_p5(self):
        """
        Raise TypeError if p is integer if nor raise typeerror.
        """
        with pytest.raises(TypeError):
            bic([1, 2, 3, 4], [5, 6, 7, 8], [12, 3])

    def test_type_y_ypred3(self):
        """
        Raise TypeError if y or y_pred are matrices.
        """
        with pytest.raises(Exception):
            bic([[1, 2, 3, 4],
                            [5, 6, 6, 7]], [1, 2, 3, 4], 3)

    def test_input(self):
        """
        check if input are more than the required, raise error if so.
        """
        with pytest.raises(Exception):
            bic([1], [3], [2], 3, 2)
