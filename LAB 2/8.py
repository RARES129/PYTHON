def process_strings(x=1, lista=None, flag=True):
    result = []
    for string in lista:
        aux = []
        for i in string:
            if ord(i) % x == 0 and flag == True:
                aux.append(i)
            elif ord(i) % x != 0 and flag == False:
                aux.append(i)
        if aux != []:
            result.append(aux)

    return result


def main():
    print(process_strings(2, ["test", "hello", "lab002"], False))


main()
