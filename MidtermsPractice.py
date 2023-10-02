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


def explode(number):
    exploded = list(map(int, str(number)))
    return exploded


def sumnumber(number):
    exploded_digits = explode(number)
    totalsum = sum(exploded_digits)
    return totalsum


def factors(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors


def isperfectnumber(number):
    numList = factors(number)
    perfect = sum(numList)
    if perfect != number:
        return "is not a perfect number."
    else:
        return "is a perfect number."


def isfriendlypair(number1, number2):
    # Get their factors first
    numfac1 = factors(number1)
    numfac2 = factors(number2)
    # Check their sum
    sumfac1 = sum(numfac1)
    sumfac2 = sum(numfac2)
    if sumfac1 == number2 and sumfac2 == number1:
        return f"{number1} and {number2} are friendly pairs."
    else:
        return f"{number1} and {number2} are not friendly pairs."
