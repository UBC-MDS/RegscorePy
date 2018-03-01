import pytest
from RegscorePy import RegscorePy


class Test_mallow:

    def test_k_p(self):
    ```
    check if k less than p
    ```
        with pytest.raises(Error):
            RegscorePy.mallow([1], [3],2,5)

    def test_value(self):
    ```
    check if the output is correct for a specified regression model
    ```
        assert RegscorePy.mallow(y, y_pred, 5) == 0.5


    def test_positive_p(self):
    ```
    check if p is positive
    ```
        with pytest.raises(TypeError):
            RegscorePy.mallow(y, y_pred, -1)

    def test_integer_p(self):
    ```
    check if p is integer
    ```
        with pytest.raises(TypeError):
            RegscorePy.mallow(y, y_pred, 3.3)

    def test_type_y_ypred(self):
    ```
    check if y and y_pred are vector
    ```
        with pytest.raises(TypeError):
            RegscorePy.mallow("a", [[1,2],[2,2]], 3.3)

    def test_match_y_ypred(self):
    ```
    check if y and y_pred have same length
    ```
        with pytest.raises(Error):
            RegscorePy.mallow([1,2], [1,2,3],2)

    def test_length_y_ypred(self):
    ```
    check if the length of y and y_pred is 1
    ```
        with pytest.raises(Error):
            RegscorePy.mallow([1], [3],2)
