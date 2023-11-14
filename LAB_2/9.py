def func(field):
    result = []
    column = 0
    while column < len(field[0]):
        row = 0
        max_col = float("-inf")
        while row < len(field):
            if field[row][column] <= max_col:
                result.append((row, column))
            if field[row][column] > max_col:
                max_col = field[row][column]
            row += 1
        column += 1

    return result


def main():
    field = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5],
    ]

    print(func(field))


main()
