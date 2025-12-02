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
            currentNumber -= number
            currentNumber = currentNumber%100
        else:
            print('direction is right..')
            currentNumber += number
            currentNumber = currentNumber%100
        
        print('current: ' + str(currentNumber))

        if currentNumber == 0:
            zeroCount += 1
    
    return zeroCount

if __name__ == '__main__':
    print(calculatePassword(importData()))