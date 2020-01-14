class NetMargin:
    """ Net Margin class """
    
    
    def getNetMarginGrade(self, matrixObj):
        
        """
        Gets the Net Margin grade

        Parameters
        ----------
        self : NetMargin object
        matrixObj : Object of the Matrix class

        Returns
        -------
        int : Net Margin grade
        """

        column = matrixObj.getColumnIndex("Mrg. Liq.")
        row = matrixObj.getPeriodRow("2018")
        netMarginValue = matrixObj.getPercentageValue(row, column)

        if (netMarginValue <=4):
            return netMarginValue

        elif (netMarginValue >= 5 and netMarginValue <7):
            return 5

        elif (netMarginValue >= 7 and netMarginValue <10):
            return 6

        elif (netMarginValue >= 10 and netMarginValue <15):
            return 7

        elif (netMarginValue >= 15 and netMarginValue <20):
            return 8

        elif (netMarginValue >= 20 and netMarginValue <25):
            return 9

        # >=25
        else:
            return 10