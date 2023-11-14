def palindromes(numbers):
    nr_of_palindromes = 0
    greatest_palindrome = 0
    for number in numbers:
        if str(number) == str(number)[::-1]:
            if number > greatest_palindrome:
                greatest_palindrome = number
            nr_of_palindromes += 1
    return nr_of_palindromes, greatest_palindrome


def main():
    print(palindromes([11, 999, 1234321, 5, 32]))


main()
