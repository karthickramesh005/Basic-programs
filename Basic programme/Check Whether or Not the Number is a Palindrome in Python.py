# Check Whether or Not the Number is a Palindrome in Python :
p = input("enter a number : ")
r = str(p)[::-1]

if p == r :
    print(p,"is palidrome number.")
else:
    print(p,"it was not palidrome number.")
