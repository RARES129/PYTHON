matrix = [
    ["f", "i", "r", "s"],
    ["n", "_", "l", "t"],
    ["o", "b", "a", "_"],
    ["h", "t", "y", "p"],
]

top = 0
bottom = len(matrix) - 1
right = len(matrix[0]) - 1
left = 0
while top <= bottom and left <= right:
    for i in range(left, right + 1):
        print(matrix[top][i], end="")
    top += 1
    if top <= bottom and left <= right:
        for i in range(top, bottom + 1):
            print(matrix[i][right], end="")
        right -= 1
    if top <= bottom and left <= right:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end="")
        bottom -= 1
    if top <= bottom and left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end="")
        left += 1
