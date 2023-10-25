def sort(lista):
    return sorted(lista, key=lambda x: x[1][2])


def main():
    lista = [("abc", "bcd"), ("abc", "zza")]
    print(sort(lista))


main()
