import pytest
from RegscorePy import mallow


class Test_mallow:

    def test_result1(self):
        """
        test if mallow() gives correct result
        """
        y = [1, 2, 3, 4]
        y_pred = [5, 6, 7, 8]
        y_sub = [1, 2, 3, 5]
        p = 2
        k = 3
        obs = mallow.mallow(y, y_pred, y_sub, k, p)
        exp = 0.0156
        assert round(obs,4) == 0.0156, 'The mallows Cp given y = [1,2,3,4], y_pred = [5,6,7,8], y_sub = [1,2,3,5], p = 2 and k = 3 should be 35/32 (applying statistical formula in main README)'

    def test_result2(self):
        """
        test if mallow() gives correct result when y and y_pred include negative and float
        """
        y = [0, 1, 1.1, -6]
        y_pred = [1, 0, 0.9, -6]
        y_sub = [1, 0.8, 0, -3.3]
        p = 2
        k = 3
        obs = mallow.mallow(y, y_pred, y_sub, k, p)
        exp = 4.68
        assert round(obs,2) == exp

    def test_k_p(self):
        """
        check if p less than k
        """
        with pytest.raises(Exception):
            mallow([1, 2, 3, 4], [3, 5, 5, 3], [5, 6, 7, 7], 2, 3)

    def test_positive_p(self):
        """
        check if p is positive
        """
        with pytest.raises(Exception):
            mallow([1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8], 3, -1)

    def test_integer_p(self):
        """
        check if p is integer
        """
        with pytest.raises(TypeError):
            mallow([1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8], 3, 2.3)

    def test_positive_k(self):
        """
        check if k is positive
        """
        with pytest.raises(Exception):
            mallow([1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8], -1, 3)

    def test_integer_k(self):
        """
        check if k is integer
        """
        with pytest.raises(TypeError):
            mallow([1, 2, 3, 4], [5, 6, 7, 8], [5, 6, 7, 8], 3.3, 2)

    def test_type_y(self):
        """
        check if y is vector
        """
        with pytest.raises(TypeError):
            mallow("a", [1, 2, 3, 4], [5, 6, 7, 8], 3, 2)

    def test_type_ypred(self):
        """
        check if y_pred is vector
        """
        with pytest.raises(TypeError):
            mallow([1, 2, 3, 4], "a", [5, 6, 7, 8], 3, 2)

    def test_type_ysub(self):
        """
        check if y_sub vector
        """
        with pytest.raises(TypeError):
            mallow([1, 2, 3, 4], [5, 6, 7, 8], "a", 3, 2)

    def test_match_y_ypred(self):
        """
        check if y, and y_pred have same length
        """
        with pytest.raises(Exception):
            mallow([1, 2], [1, 2, 3], [1, 2], 3, 2)

    def test_match_y_ysub(self):
        """
        check if y, and y_sub have same length
        """
        with pytest.raises(Exception):
            mallow([1, 2], [1, 2], [1, 2, 3], 3, 2)

    def test_length_y_ypred(self):
        """
        check if the length of y, y_sub, and y_pred is 1
        """
        with pytest.raises(Exception):
            mallow([1], [3], [2], 3, 2)

    def test_empty_y(self):
        """
        check if the y is empty
        """
        with pytest.raises(Exception):
            mallow([],[1,2,3,4],[5,6,7,8],3,2)

    def test_empty_y_pred(self):
        """
        check if the y_pred is empty
        """
        with pytest.raises(Exception):
            mallow([1,2,3,4],[],[5,6,7,8],3,2)
