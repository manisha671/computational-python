import random
import time
import os

north = {'x': 0, 'y': 1}
south = {'x': 0, 'y': -1}
east = {'x': 1, 'y': 0}
west = {'x': -1, 'y': 0}

areaX = 20
areaY = 20

posX = 9
posY = 9

loopFor = 100

previousPath = {}

while(loopFor > 0):
    finalArea = []
    for i in range(0, areaY-1):
        newArr = []
        for j in range(0, areaX-1):
            insertCharacter = '-'
            if (i == posY and j == posX):
                insertCharacter = '*'
            newArr.append(insertCharacter)
        finalArea.append(newArr)

    for i in range(len(finalArea)):
        print(finalArea[i])

    sampleDirection = random.sample([north, south, east, west], 1)

    posX = sampleDirection[0].get('x') + posX
    posY = sampleDirection[0].get('y') + posY

    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

    loopFor -= 1
