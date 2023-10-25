def count_unique_and_duplicates(lst):
    unique = len(set(lst))
    duplicates = len(lst) - unique
    return (unique, duplicates)


def main():
    lst = [1, 2, 3, 4, 5, 5, 5, 6, 7, 7]
    unique, duplicates = count_unique_and_duplicates(lst)
    print("Unique:", unique)
    print("Duplicates:", duplicates)


main()
