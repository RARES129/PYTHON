class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for j in range(m)] for i in range(n)]

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("NU SE POATE MULTIPLICA, GHINION :((")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                value = 0
                for k in range(self.m):
                    value += self.get(i, k) * other.get(k, j)
                result.set(i, j, value)
        return result

    def transform(self, function):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, function(self.get(i, j)))


def main():
    matrix = Matrix(2, 3)
    matrix.set(0, 0, 1)
    matrix.set(0, 1, 2)
    matrix.set(0, 2, 3)
    matrix.set(1, 0, 4)
    matrix.set(1, 1, 5)
    matrix.set(1, 2, 6)

    print("MATRICEA ORIGINALA:")
    for i in range(matrix.n):
        for j in range(matrix.m):
            print(matrix.get(i, j), end=" ")
        print()

    transposed = matrix.transpose()
    print("MATRICEA TRANSPUSA:")
    for i in range(transposed.n):
        for j in range(transposed.m):
            print(transposed.get(i, j), end=" ")
        print()

    other = Matrix(3, 2)
    other.set(0, 0, 7)
    other.set(0, 1, 8)
    other.set(1, 0, 9)
    other.set(1, 1, 10)
    other.set(2, 0, 11)
    other.set(2, 1, 12)

    multiplied = matrix.multiply(other)
    print("MATRICEA MULTIPLICATA:")
    for i in range(multiplied.n):
        for j in range(multiplied.m):
            print(multiplied.get(i, j), end=" ")
        print()

    matrix.transform(lambda x: x * 2)
    print("MATRICEA TRANSFORMATA:")
    for i in range(matrix.n):
        for j in range(matrix.m):
            print(matrix.get(i, j), end=" ")
        print()


main()
