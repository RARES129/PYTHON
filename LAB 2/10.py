def generate_tuple(*lists):
    result = []
    for index1 in range(max(len(index1) for index1 in lists)):
        aux = []
        for index2 in lists:
            if index1 < len(index2) and index2[index1] != None:
                aux += [index2[index1]]
        result.append(tuple(aux))
    return result


def main():
    print(generate_tuple([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
    # print(generate_tuple([1, 2, 3], [7], ["a", "c"]))


main()
