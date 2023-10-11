string1 = input()
string2 = ""
for index in range(len(string1)):
    if string1[index].isupper():
        string2 = string2 + string1[index].lower() + "_"
    else:
        string2 = string2 + string1[index]
print(string2)
