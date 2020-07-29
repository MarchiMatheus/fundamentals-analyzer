class NetProfit:
    """ Net Profit class """

    def getNetProfitGrade(self, matrixObj, year):

        """
        Gets the Net Profit grade

        Parameters
        ----------
        self : NetProfit object
        matrixObj : Object of the Matrix class
        year : Year to calculate the grade

        Returns
        -------
        int : Net Profit grade
        """

        column = matrixObj.getColumnIndex("Lucro Liq.")
        yearRowIndex = 2
        lastRow = matrixObj.getPeriodRow(year)

        totalOfComparisons = 0
        netProfitBiggerThanPreviousCount = 0
        
        #Execute the comparison between the year (beggining with the first one)
        # and the following year until the last year informed (lastRow)
        while (yearRowIndex <= lastRow):

            year = matrixObj.getValue(yearRowIndex, 0)
            netProfit = matrixObj.getValue(yearRowIndex, column)
            previousNetProfit = matrixObj.getValue(yearRowIndex-1, column)

            #Count if the current net profit is bigger than zero
            # and if it's bigger or equal to the last year net profit
            if (netProfit > 0 and netProfit >= previousNetProfit):
                netProfitBiggerThanPreviousCount += 1            

            totalOfComparisons += 1
            yearRowIndex += 1
        
        #print(str(netProfitBiggerThanPreviousCount) + '/' + str(totalOfComparisons))
        profitImprovedPercentage = (netProfitBiggerThanPreviousCount/totalOfComparisons) * 100
        
        #Percentage below 10%
        if(profitImprovedPercentage <= 10):
            return 0

        #Percentage is 100%
        elif (profitImprovedPercentage == 100):
            return 10

        #Percentage between 11% and 99%
        else:
            firstValue = str(profitImprovedPercentage)[0]
            return int(firstValue)