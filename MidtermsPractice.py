import math


def ispalindrome(number):
    check = number.isnumeric()
    if check:
        print("Valid Number")
        if number == number[::-1]:
            return "The Number is Palindrome"
        else:
            return "The Number is not Palindrome"
    else:
        return "The Input is not a number"


def isprime(number):
    if number <= 1:
        return "Not A Prime Number"
    else:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return "Not A Prime Number"
        return "Prime Number"


def sumnumber(number):
    explode = list(map(int, str(number)))
    totalsum = sum(explode)
    return totalsum
