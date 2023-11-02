class XoModel:
    matrix = []
    size = 0

    def __init__(self, size):
        self.size = size
        for x in range(size):
            y = []
            self.matrix.append(y)
            for _ in range(size):
                if _ < size:
                    self.matrix[x].append('-')

    
    def __str__(self):
        matrixString = ''
        for x in range(len(self.matrix)):
            matrixString += f'{x+1}. '
            matrixString += ' '.join(list(map(str, self.matrix[x])))
            matrixString += '\n'
        return matrixString
    
    def set(self, row, cells, symbol):
        self.matrix[row][cells] = symbol

    def row(self, row):
        return tuple(self.matrix[row]) 

    def col(self, col):
        column = []
        for i in range(len(self.matrix)):
            column.append(self.matrix[i][col])
        return tuple(column)

    def diag(self, side):
        word = []
        if side == 1:
            for i in range(len(self.matrix)):
                for x in range(len(self.matrix[i])):
                    if i < x:
                        continue
                    elif i > x:
                        continue
                    else:
                        word.append(self.matrix[i][x])
            return tuple(word)
        else:
            for y in range(len(self.matrix)):
                length = len(self.matrix[y])
                index = length - y - 1
                word.append(self.matrix[y][index])
            return tuple(word)

    def is_empty(self, row, col):
        if self.matrix[row][col] == '-':
            return True
        else:
            return False

if __name__ == '__main__':
    xomodel = XoModel(5)
    xomodel.set(1, 1, 'X')
    print(xomodel)
    print(xomodel.row(2))
    print(xomodel.col(1))
    print(xomodel.diag(1))
