def counter(*lists, x):
    # new_list = [i for list in lists for i in list]
    new_list  = list(set(new_list))

    result = []
    count = 0
    for i in new_list:
        for l in lists:
            if i in l:
                count += l.count(i)
        if count == x:
            result.append(i)
        count = 0
    
    return result

def main():
    print(counter([1,2,3], [2,3,4],[4,5,6], [4,1, "test"], x = 2))

main()