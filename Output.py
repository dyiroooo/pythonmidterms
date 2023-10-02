import MidtermsPractice

# Problem 1
print("Palindrome Checker")
unumber = str(input("Enter A Number: "))
print("Result: ", MidtermsPractice.ispalindrome(unumber))
print("")

# Problem 2
print("Prime Number Checker")
primenumber = int(input("Enter A Number: "))
print("Result: ", MidtermsPractice.isprime(primenumber))
print("")

# Problem 3
print("Explode and Sum")
esNumber = str(input("Enter A Number: "))
output = MidtermsPractice.sumnumber(esNumber)
print("Total Sum: ", output)
print("")

# Problem 4
print("Perfect Number Checker")
perfNumber = int(input("Enter A Number: "))
factorsum = sum(MidtermsPractice.factors(perfNumber))
print("Factor: ", MidtermsPractice.factors(perfNumber), " = ", factorsum)
print(perfNumber, MidtermsPractice.isperfectnumber(perfNumber))
print("")

# Problem 5
print("Friendly Pair Number Checker")
num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
print(MidtermsPractice.isfriendlypair(num1, num2))
