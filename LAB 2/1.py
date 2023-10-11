def fibonacci(n):
    list = []
    if n == 1:
        list.append(1)
    else:
        list.append(1)
        list.append(1)
        for i in range(2, n):
            list.append(list[i - 1] + list[i - 2])
    return list


n = input()
print(fibonacci(int(n)))
