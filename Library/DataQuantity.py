class DataQuantity:
    """ Data Quantity class """

    def getDataQuantityGrade(self, matrixObj):

        """
        Gets the Data Quantity grade
        Rules:
            Less than 5 year data: Grade 7
            Between 5 and 7: Grade 8
            Between 8 and 10: Grade 9
            Bigger than 10 years: Grade 10

        Parameters
        ----------
        self : DataQuantity object
        matrixObj : Object of the Matrix class

        Returns
        -------
        int : Data Quantity grade
        """
        
        lastYear = matrixObj.getValue(-1, 0)
        quantityOfData = matrixObj.getPeriodRow(str(lastYear))

        if (quantityOfData < 5):
            return 7

        elif (quantityOfData >= 5 and quantityOfData <= 7):
            return 8

        elif (quantityOfData >= 8 and quantityOfData < 10):
            return 9

        # quantityOfData >= 10
        else:
            return 10