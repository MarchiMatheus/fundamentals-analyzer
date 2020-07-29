import os
import re

#Private library
from API.Calculation import Calculation


#Returns all files from the given path
def getAllFiles(path):
    return os.listdir(path)


#Creates a result .csv file with the companies and it's respectives grades
def createResutFile(result):

    f = open("./Result/result.csv", "a")

    for row in result:
        f.write(row + '\n')
    
    f.close()


#Main function to execute the program
def main(company, year):

    #Calculates the average grade
    averageGrade = Calculation(company).calculateAverageGrade(year)

    print()
    print(company + ' - Average Grade: %.2f' %averageGrade)

    # matrixObj = Matrix("./Companies CSV/" + company + ".csv")
    # dataQuantity = DataQuantity().getDataQuantityGrade(matrixObj)
    # print (dataQuantity)


#Process all files in Companies CSV folder and
def processAll():
    
    fileFolder = "./Companies CSV/"
    allFiles = getAllFiles(fileFolder)
    result = []

    print()
    for company in allFiles:
        
        companyNamePattern = "(.*).csv"
        companyName = re.match(companyNamePattern, company).group(1)
        averageGrade = Calculation(companyName).calculateAverageGrade()

        # print(companyName + ' - Average Grade: %.2f' %averageGrade)

        #Insert values in the result array
        result.append(companyName + ', %.2f' %averageGrade)
    
    createResutFile(result)


#Execute main function
if __name__ == '__main__':
    company = input("Enter the company ticker to analyze: ")
    year = input("Enter the year to analyze: ")
    main(company, year)
    #processAll()