def extract(string):
    test = False
    result = 0
    for index in string:
        if test == True:
            if index.isdigit():
                result = result * 10 + int(index)
            else:
                break
        if test == False:
            if index.isdigit():
                result = int(index)
                test = True
    return result


string = input()
print(extract(string))
