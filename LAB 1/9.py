def most_common(string):
    string = string.lower()
    list_of_letters = []
    max_frequency = 0
    most_common_letter = ""
    for index in string:
        if index.isalpha():
            list_of_letters.append(index)
    for index in list_of_letters:
        if list_of_letters.count(index) > max_frequency:
            max_frequency = list_of_letters.count(index)
            most_common_letter = index
    return most_common_letter


string = input()
print(most_common(string))
