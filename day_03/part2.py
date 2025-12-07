import string, re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray


def calculateJoltage(inputDataArray):

    joltage = 0

    for line in inputDataArray:
        #print(line)
        highestNumber = calculateHighestNum(line,12)
        #print('highest: ',highestNumber)
        joltage += highestNumber

    return joltage

def calculateHighestNum(sourceNumber,length):

    if len(sourceNumber) == length:
        return sourceNumber
    
    if length == 1:
        lineSplit = list(sourceNumber)
        lineSplit.sort(reverse=True)
        highestNum = lineSplit[0]
        return highestNum

    splitLine = sourceNumber[:(length*-1)+1]
    #print('inputLine: ', sourceNumber,' splitline: ',splitLine, ' ... length was: ',length)
    lineSplit = list(sourceNumber[:(length*-1)+1])
    lineSplit.sort(reverse=True)
    highestNum = lineSplit[0]

    for x in range(len(splitLine)):
        #print(splitLine[x])
        currentNum = splitLine[x]
        if int(currentNum) == int(highestNum):
            newSearchString = sourceNumber[x+1:]
            #print('newSearchString: ',newSearchString)
            highestTrailing = calculateHighestNum(newSearchString,length-1)
            newNumber = int(str(currentNum) + str(highestTrailing))
            return newNumber
    
    return 0

if __name__ == '__main__':
    print(calculateJoltage(importData()))