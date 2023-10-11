import math
def gcd(m,n):
    while m!=n:
        if m>n: m = m - n
        else: n = n - m
    return m

numbers = input().split()
numbers = [int(num) for num in numbers]

tempGCD=gcd(numbers[0],numbers[1])

for index in numbers:
    GCD=gcd(tempGCD,index)

print(GCD)


