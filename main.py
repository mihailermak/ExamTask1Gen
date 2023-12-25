import random

def generation(size):
    array = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(i+1, size):
            array[i][j] = random.randint(0, 1)
            array[j][i] = array[i][j]
    return array

def checkmatrix(array):
    for row in array:
        count = sum(row)
        if not (count >= 2 and count <= 5):
            return False
    return True

size = 8
resultmatrix = generation(size)
while not checkmatrix(resultmatrix):
    resultmatrix = generation(size)

for row in resultmatrix:
    print(row)
