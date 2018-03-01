## Add code to test AIC function
class test_aic:
    def y_ypred_len():
        """
        test if y and y_pred have same length, if not yield error
        """
        with pytest.raises(Error):
            RegscorePy.aic([1,2,3,4],[4,5,6,7,8], 3)
