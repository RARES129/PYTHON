def prime(list):
    new_list = []
    for index in list:
        flag = False
        if index > 1:
            for i in range(2, index):
                if (index % i) == 0:
                    flag = True
                    break
            if flag == False:
                new_list.append(index)
    return new_list


list = input().split()
list = [int(index) for index in list]
print(prime(list))
