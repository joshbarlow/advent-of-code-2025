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

        highestSecond = 0
        
        lineSplit = list(line[:-1])
        lineSplit.sort(reverse=True)
        highestNum = lineSplit[0]

        #print('highest =' + str(highestNum))

        lineSplit = list(line)

        for x in range(len(lineSplit)-1):
            if lineSplit[x] == highestNum:
                secondSplit = lineSplit[x+1:]
                #print('secondSplit =', secondSplit)
                secondSplit.sort(reverse=True)
                if int(secondSplit[0]) > int(highestSecond):
                    highestSecond = secondSplit[0]
                
        joltage += int(str(highestNum) + str(highestSecond))
    return joltage

if __name__ == '__main__':
    print(calculateJoltage(importData()))