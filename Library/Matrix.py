########## Install Numpy ##########
### python -m pip install numpy ###
###################################

import re
import csv
import numpy

class Matrix():
    """ This class represents the CSV file in a matrix """


    #Constructor
    def __init__(self, filePath):

        """
        Matrix constructor
        Creates a matrix with the given csv file

        Parameters
        ----------
        self : Matrix class object
        filePath : Path to the file that will be converted into a matrix        
        """

        reader = csv.reader(open(filePath, "r"), delimiter = ",")
        x = list(reader)
        self.matrix = numpy.array(x)
    

    def getColumnIndex(self, columnName):
        
        """
        Gets the column index based in the column name passed as argument

        Parameters
        ----------
        self : Matrix class object
        columnName : Text with the column name to be found

        Returns
        -------
        int : The column index in the matrix
        """

        columnIndex = -1
        
        for field in self.matrix[0]:
            columnIndex += 1
            if (field == columnName):
                break

        return columnIndex


    def getPeriodRow(self, period):
        """
        Gets the matrix year row index

        Parameters
        ----------
        self : Matrix class object
        period : The given period. i.e. 2018, 2T2017, etc

        Returns
        -------
        int : The period row index (Zero based index)
        """
        
        periodIndex = 1

        while self.matrix[periodIndex][0] != period:
            periodIndex += 1

        return periodIndex
        

    def getPercentageValue(self, row, column):

        """
        Returns the matrix value in the given row and column position
        Note: The specified position in the matrix has to be an percentage value
            Otherwise, the returned number won't be correct

        i.e.
            15% -> returns '15'
            1.145 -> returns '1'
        
        Parameters
        ----------
        self : Matrix class object
        row : Zero based row index of the matrix
        column : Zero based column index of the matrix

        Returns
        -------
        int : The numeric value at the given position of the matrix
        """

        return int(re.match("(\d+)", self.matrix[row][column]).group(0))


    def getValue(self, row, column):

        """
        Returns the matrix value in the given row and column position
        
        Parameters
        ----------
        self : Matrix class object
        row : Zero based row index of the matrix
        column : Zero based column index of the matrix

        Returns
        -------
        int : The numeric value at the given position of the matrix
        """

        return int((self.matrix[row][column]).replace(".", ""))