def group_by_rhyme(lista):
    listaa = lista[:]
    result = []
    for i in listaa:
        for j in listaa:
            if i != j and i[-2:] == j[-2:]:
                result.append([i, j])
                listaa.remove(i)
                listaa.remove(j)
                break
    
    for i in listaa:
        result.append([i])

    return result


def main():
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))

main()