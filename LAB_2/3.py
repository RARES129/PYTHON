def operations(a, b):
    a = set(a)
    b = set(b)
    a_intersected_b = a & b
    a_reunited_b = a | b
    a_minus_b = a - b
    b_minus_a = b - a
    return a_intersected_b, a_reunited_b, a_minus_b, b_minus_a


# De transformat din set in lista cu list()

a = input().split()
b = input().split()
print(operations(a, b))
