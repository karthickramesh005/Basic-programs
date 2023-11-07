# Factorial of a Number in Python :

n = int(input("Enter a number : "))
f = 1

if n < 0 :
    print("Its a negative number")
else:
    for i in range(1,n + 1):
        f *= i
print("Factorial of ",n," of ",f)
        
