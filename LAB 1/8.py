def countBits(number):
    binary = bin(int(number))
    count = 0
    for index in binary:
        if index == "1":
            count += 1
    return count


number = input()
print(countBits(number))
