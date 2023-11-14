def replace_under_main_diag(matrix):
    index1 = 1
    index2 = 1
    while index1 < len(matrix) and index2 < len(matrix[0]):
        for index in range(0, index2):
            matrix[index1][index] = 0
        index1 += 1
        index2 += 1
    return matrix


def main():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    print(replace_under_main_diag(matrix))


main()
