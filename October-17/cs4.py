class Matrix:
    matrix = []
    current_row = 0

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        for x in range(rows):
            y = []
            self.matrix.append(y)
            for _ in range(cols):
                self.matrix[x].append(0)

    def __next__(self):
        yield self.matrix[self.current_row]
        self.current_row += 1

    def set(self, row, cells):
        for x in range(len(cells)):
            self.matrix[row][x] = cells[x]

    def show(self):
        print(self.matrix)

matrix = Matrix(3, 4)
matrix.show()

matrix.set(1, [1, 2, 3, 4])
matrix.show()

for _ in range(3):
    print(matrix)

matrix_example = [[1, 2, 3],
                  [4, 5, 6]]

