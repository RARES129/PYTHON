def func(field):
    result = []
    j = 0
    while j < len(field[0]):
        i = 1
        max_col = field[0][j]
        while i < len(field):
            if field[i][j] <= max_col:
                result.append((i, j))
            if field[i][j] > max_col:
                max_col = field[i][j]
            i += 1
        j += 1
    
    return result

def main():
    field = [[1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 7, 2],
            [5, 5, 2, 5, 6, 4],
            [6, 6, 7, 6, 7, 5]] 
    
    print(func(field))

main()