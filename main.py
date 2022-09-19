import numpy as np


def inverseMatrix(origMatrix):
    size = len(origMatrix[0])
    A = origMatrix
    E = np.eye(size)
    print('Ед матрица\n', E)
    A_inv = []
    for i in E:
        A_inv.append(invCalc(A, i))
    print('\nИнверсированная матрица')
    print(A_inv)



def invCalc(originMatrix, E):
    extended = createExtended(originMatrix, E)
    print('Расширенная\n', extended)
    uMatrix, zMatrix = getUZ(extended)
    print('U матрица:\n', uMatrix)
    print()
    print('Z матрица:\n', zMatrix)
    xlist = getX(zMatrix, len(originMatrix))
    return xlist


def createExtended(original, data):
    size = len(original[0])
    extended = np.zeros((size + 1, size + 1))
    for i in range(size + 1):
        for j in range(size + 1):
            if i < size and j < size:
                extended[i][j] = original[i][j]
            if i == size and j < size:
                extended[i][j] = 0
            extended[i][size] = 1
            # extended[i][size - 1] = 1
        if i < size and j == size:
            if (data[i] == 0):
                extended[i][size] = data[i]
            else:
                extended[i][size] = data[i] * -1
    return extended


def ortoMethod(size, list1, list2):
    M = size
    Matrix = np.array(list1)
    bMatrix = list2
    extendedMatrix = createExtended(Matrix, bMatrix)
    uzi(extendedMatrix, Matrix)


def getUZ(aMatrix):
    size = len(aMatrix)

    uMatrix = np.zeros((size, size))
    zMatrix = np.zeros((size, size))
    for i in range(size):
        uMatrix[i] = aMatrix[i]
        for j in range(i):
            uMatrix[i] = uMatrix[i] - (np.dot(aMatrix[i], zMatrix[j]) * zMatrix[j])
        zMatrix[i] = uMatrix[i] / np.sqrt(np.dot(uMatrix[i], uMatrix[i]))
    return uMatrix, zMatrix


def uzi(aMatrix, Matrix):
    size = len(Matrix[0])
    uMatrix, zMatrix = getUZ(aMatrix)

    xList = getX(zMatrix, size)
    VectorNevyaz = np.dot(Matrix, xList) - bMatrix

    with open('Out.txt', 'w', encoding='UTF-8') as file:
        file.write('a matrix: \n' + str(Matrix) + '\n\n')
        file.write('b vector: \n' + str(bMatrix) + '\n\n')
        file.write('A matrix: \n' + str(aMatrix) + '\n\n')
        file.write('U matrix: \n' + str(uMatrix) + '\n\n')
        file.write('Z matrix: \n' + str(zMatrix) + '\n\n')
        file.write('x: =  \n')
        for i in range(size):
            file.write('X[' + str(i) + '] = ' + str(xList[i]) + '\n')
        file.write('\nВектор невязки: ' + str(VectorNevyaz) + '\n\n')
        file.write('Норма невязки : ' + str(np.sqrt((VectorNevyaz ** 2).sum())))
        file.write('FSDFSDFSDFSDFSDFSDFSDFSD')


def getX(zMatrix, size):
    x = 0
    xList = []
    for i in range(size):
        x = zMatrix[-1][i] / zMatrix[-1][-1]
        xList.append(x)
    return xList


if __name__ == '__main__':
    print('Славка ку')
    aMatrix = []
    bMatrix = []
    with open('in.txt', encoding='UTF-8') as file:
        split_file = file.read().splitlines()
        for line in split_file:
            split_line = list(map(int, line.split(' ')))
            bMatrix.append(split_line[-1])
            split_line.pop()
            aMatrix.append(split_line)

    M = len(bMatrix)

    ortoMethod(M, aMatrix, bMatrix)
    inverseMatrix(aMatrix)
