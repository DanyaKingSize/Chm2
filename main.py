import numpy as np


def inverseMatrix(aMatrix,size):
    E = np.eye(size)
    A_inv = np.zeros_like(aMatrix)
    for i in range(size):
        uzi(aMatrix, E[:, i])





def createExtended(original, size, data):
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
            extended[i][size] = data[i] * -1
    return extended


def ortoMethod(size, list1, list2):
    M = size
    Matrix = np.array(list1)
    bMatrix = list2
    extendedMatrix = createExtended(Matrix, M, bMatrix)

    print(aMatrix)
    print()
    print(extendedMatrix)

    uzi(M, extendedMatrix, Matrix)


def uzi(size, aMatrix, Matrix):
    uMatrix = np.zeros((size + 1, size + 1))
    zMatrix = np.zeros((size + 1, size + 1))
    for i in range(size + 1):
        uMatrix[i] = aMatrix[i]
        for j in range(i):
            uMatrix[i] = uMatrix[i] - (np.dot(aMatrix[i], zMatrix[j]) * zMatrix[j])
        zMatrix[i] = uMatrix[i] / np.sqrt(np.dot(uMatrix[i], uMatrix[i]))
    print()
    print()
    print('U matrix:\n')

    print(uMatrix, '\n\n')

    print('Z matrix: ')
    print(zMatrix)
    x = 0
    xList = []
    print('X: = ')
    VectorNevyaz = Matrix
    for i in range(size):
        x = zMatrix[size][i] / zMatrix[size][size]
        print('x(', i, ' )  = ', x)
        xList.append(x)
    VectorNevyaz = np.dot(Matrix, xList) - bMatrix

    print('Вектора невязки')
    print(VectorNevyaz)
    inverseMatrix(Matrix,size)

    with open('Out.txt', 'w', encoding='UTF-8') as file:
        file.write('a matrix: \n' + str(Matrix) + '\n\n')
        file.write('b vector: \n' + str(bMatrix) + '\n\n')
        file.write('A matrix: \n' + str(aMatrix) + '\n\n')
        file.write('U matrix: \n' + str(uMatrix) + '\n\n')
        file.write('Z matrix: \n' + str(zMatrix) + '\n\n')
        file.write('x: =  \n')
        for i in range(size):
            file.write('X[' + str(i) + '] = ' + str(xList[i])+ '\n')
        file.write('\nВектор невязки: ' + str(VectorNevyaz)+'\n\n')
        file.write('Норма невязки : ' + str(np.sqrt((VectorNevyaz**2).sum())))


if __name__ == '__main__':
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
