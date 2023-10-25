def nr_of_palindromes(numbers):
    nr_of_palindromes = 0
    for number in numbers:
        if str(number) == str(number)[::-1]:
            nr_of_palindromes += 1
    return nr_of_palindromes

def greatest_palindrome(numbers):
    maxim = 0
    for i in numbers:
        if str(i) == str(i)[::-1]:
            if i > maxim:
                maxim = i

    return maxim

def return_tuple(numbers):
    return (nr_of_palindromes(numbers), greatest_palindrome(numbers))

def main():
    print(return_tuple([11, 999, 1234321, 5, 32]))

main()