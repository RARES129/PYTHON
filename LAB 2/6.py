def counter(*lists, x):
    new_list = set([i for list in lists for i in list])

    result = []
    count = 0
    for index1 in new_list:
        for index2 in lists:
            if index1 in index2:
                count += index2.count(index1)
        if count == x:
            result.append(index1)
        count = 0

    return result


def main():
    print(counter([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], x=2))


main()
