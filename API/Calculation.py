#Private library
from Library.Matrix import Matrix
from Library.DataQuantity import DataQuantity

from Library.Fundamentals.Roe import Roe
from Library.Fundamentals.Payout import Payout
from Library.Fundamentals.NetMargin import NetMargin
from Library.Fundamentals.NetProfit import NetProfit


class Calculation:

    """ Calculation class """
    

    #Constructor
    def __init__(self, company):
        
        """
        Calculation constructor
        Execute the grade calculation for the given company

        Parameters
        ----------
        self : Calculation class object
        company : Company name
        """

        fileFolder = "./Companies CSV/"

        #Creates the matrix object based on the .csv source file
        self._matrixObj = Matrix(fileFolder + company + ".csv")


    def calculateAverageGrade(self):
        
        """
        Calculates the average between the fundamentals:
            - ROE
            - Payout
            - Net Margin
            - Net Profit

        Quantity of available data to analize is also added to the grade logic

        Parameters
        ----------
        self : Calculation class object

        Returns
        -------
        int : The fundamentals average grade
            -1 if an error has occured
        """
        
        try:

            #Calculate the grades
            roeGrade = Roe().getROEGrade(self._matrixObj)
            payoutGrade = Payout().getPayoutGrade(self._matrixObj)
            netMarginGrade = NetMargin().getNetMarginGrade(self._matrixObj)
            netProfit = NetProfit().getNetProfitGrade(self._matrixObj)
            dataQuantity = DataQuantity().getDataQuantityGrade(self._matrixObj)

            # print('ROE: ' + str(roeGrade) +
            #       ', Payout: ' + str(payoutGrade) +
            #       ', Net Margin: ' + str(netMarginGrade) +
            #       ', Net Profit: ' + str(netProfit) +
            #       ', Data Quantity: ' + str(dataQuantity))

            #Calculates the average grade
            return ((roeGrade + payoutGrade + netMarginGrade + netProfit + dataQuantity)/5)

        except:
            return -1