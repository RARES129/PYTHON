def set_operations(*sets):
    operations = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            key1 = str(set1) + " | " + str(set2)
            key2 = str(set1) + " & " + str(set2)
            key3 = str(set1) + " - " + str(set2)
            key4 = str(set2) + " - " + str(set1)
            operations[key1] = set(set1) | set(set2)
            operations[key2] = set(set1) & set(set2)
            operations[key3] = set(set1) - set(set2)
            operations[key4] = set(set2) - set(set1)
    return operations


# Example usage:
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
result = set_operations(set1, set2, set3)
print(result)
