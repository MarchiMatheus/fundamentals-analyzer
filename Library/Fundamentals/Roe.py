class Roe:
    """ Return on Equity(ROE) class """
    
    
    def getROEGrade(self, matrixObj, year):

        """
        Gets the Return on Equity grade

        Parameters
        ----------
        self : ROE object
        matrixObj : Object of the Matrix class
        year : Year to calculate the grade

        Returns
        -------
        int : Return on Equity grade
        """

        column = matrixObj.getColumnIndex("ROE")
        row = matrixObj.getPeriodRow(year)
        roeValue = matrixObj.getPercentageValue(row, column)
        
        if (roeValue <=4):
            return roeValue

        elif (roeValue >= 5 and roeValue <7):
            return 5

        elif (roeValue >= 7 and roeValue <10):
            return 6

        elif (roeValue >= 10 and roeValue <15):
            return 7

        elif (roeValue >= 15 and roeValue <20):
            return 8

        elif (roeValue >= 20 and roeValue <25):
            return 9

        # >=25
        else:
            return 10