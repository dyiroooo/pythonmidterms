import MidtermsPractice

# Problem 1
print("Palindrome Checker")
unumber = str(input("Enter A Number: "))
print(MidtermsPractice.ispalindrome(unumber))
print("")
# Problem 2
print("Prime Number Checker")
primenumber = int(input("Enter A Number: "))
print(MidtermsPractice.isprime(primenumber))
print("")
# Problem 3
print("Explode and Sum")
esNumber = str(input("Enter A Number: "))
output = MidtermsPractice.sumnumber(esNumber)
print("Total Sum: ", output)
