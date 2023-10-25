def list_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    a_diff_b = set(a) - set(b)
    b_diff_a = set(b) - set(a)
    return [intersection, union, a_diff_b, b_diff_a]


def main():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    print(list_operations(a, b))


main()
