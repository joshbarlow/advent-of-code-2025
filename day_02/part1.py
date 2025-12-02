import string, re

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    splitSections = cleanInputDataArray[0].split(',')
    return splitSections


def calculateIDS(inputDataArray):

    badID_count = 0

    for line in inputDataArray:
        print(line)
        lineSplit = line.split('-')
        intRange = list(range(int(lineSplit[0]), int(lineSplit[1])+1))
        for x in intRange:
            if len(str(x)) % 2 == 0:
                print(x,' is even')
                if (str(x)[:int(len(str(x))/2)]) == (str(x)[int(len(str(x))/2):]):
                    print('repeat: ', x)
                    badID_count += x

    return badID_count

if __name__ == '__main__':
    print(calculateIDS(importData()))