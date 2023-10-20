class Matrix:
    matrix = []
    current_row = -1
    rows = 0
    cols = 0

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

        for x in range(rows):
            y = []
            self.matrix.append(y)
            for _ in range(cols):
                if _ < cols:
                    self.matrix[x].append(0)

    def __iter__(self):
        return self

    def __repr__(self):
        matrixString = ''
        for x in range(len(self.matrix)):
            matrixString += ', '.join(list(map(str, self.matrix[x])))
            matrixString += '\n'
        return matrixString

    def __add__(self, other):
        newMatrix = []
        for x in range(len(self.matrix)):
            emptyList = []
            newMatrix.append(emptyList)
            for y in range(self.cols):
                newMatrix[x].append(self.matrix[x][y] + other.matrix[x][y])
        return newMatrix
        
    def __next__(self):
        if self.rows - 1 > self.current_row:
            self.current_row += 1
            return self.matrix[self.current_row]
        else:
            raise StopIteration

    def set(self, row, cells):
        for x in range(len(cells)):
            self.matrix[row][x] = cells[x]

    def show(self):
        print(self.matrix)

    def transposed(self):
        transporedMatrix = []
        for x in range(self.cols):
            emptyList = []
            transporedMatrix.append(emptyList)
            for y in range(self.rows):
                transporedMatrix[x].append(self.matrix[y][x])
        return transporedMatrix

matrix = Matrix(3, 4)

matrix.set(1, [1, 2, 3, 4])
matrix.set(2, [5, 6, 7, 8])

print(matrix)

matrix_2 = Matrix(3, 4)

matrix_2.set(0, [0, 2, 4, 5])
matrix_2.set(1, [5, 76, 12, 3])
matrix_2.set(2, [22, 778, 34, 6])

add = matrix + matrix_2

print(matrix_2)
print(add)

print(matrix.transposed())


# for x in matrix:
#     print(x)