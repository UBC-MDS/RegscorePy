import pytest
from RegscorePy import RegscorePy


class Test_bic:

    def test_type_y_ypred(self):
    ```
    check if y and y_pred are vector
    ```
        with pytest.raises(TypeError):
            RegscorePy.bic("a", [[1,2],[2,2]], 3.3)



