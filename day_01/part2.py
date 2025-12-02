import string

def importData():
    with open('input.txt') as input_file:
        inputDataArray = input_file.readlines()
    cleanInputDataArray = []
    for line in inputDataArray:
        cleanInputDataArray.append(line.replace("\n", ""))
    return cleanInputDataArray

def calculatePassword(inputDataArray):

    currentNumber = 50
    zeroCount = 0

    for line in inputDataArray:
        direction = line[:1]
        number = int(line[1:])

        if direction == 'L':
            print('direction is left..')
            for x in range(number):
                currentNumber -= 1
                currentNumber = currentNumber%100
                if currentNumber == 0:
                    zeroCount += 1

        else:
            print('direction is right..')
            for x in range(number):
                currentNumber += 1
                currentNumber = currentNumber%100
                if currentNumber == 0:
                    zeroCount += 1
    
    return zeroCount

if __name__ == '__main__':
    print(calculatePassword(importData()))