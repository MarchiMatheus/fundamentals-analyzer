class Payout:
    """ Payout class """
    
    
    def getPayoutGrade(self, matrixObj):
        
        """
        Gets the Payout grade

        Parameters
        ----------
        self : Payout object
        matrixObj : Object of the Matrix class

        Returns
        -------
        int : Payout grade
        """

        column = matrixObj.getColumnIndex("Payout")
        row = matrixObj.getPeriodRow("2018")
        payoutValue = matrixObj.getPercentageValue(row, column)

        if (payoutValue < 1):
            return 0

        elif (payoutValue >= 1 and payoutValue < 10):
            return 1

        elif (payoutValue >= 10 and payoutValue < 20):
            return 2
        
        elif (payoutValue >= 20 and payoutValue < 30):
            return 3

        elif (payoutValue >= 30 and payoutValue < 40):
            return 4

        elif (payoutValue >= 40 and payoutValue < 50):
            return 5

        elif (payoutValue >= 50 and payoutValue < 60):
            return 6

        elif (payoutValue >= 60 and payoutValue < 70):
            return 7

        elif (payoutValue >= 90):
            return 8

        elif (payoutValue >= 80 and payoutValue < 90):
            return 9

        # >= 70 and <80
        else:
            return 10