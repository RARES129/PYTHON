def generate_tuple(*lists):    
    result = []
    for i in range(max(len(i) for i in lists)):
        aux = []
        for j in lists:
            if i < len(j) and j[i] != None:
                aux += [j[i]]

        result += [tuple(aux)]
    return result    

def main():
    print(generate_tuple([1,2,3], [5,6,7], ["a", "b", "c"]))
    # print(generate_tuple([1,2,3,4], [7], ["a", "c"]))

main()