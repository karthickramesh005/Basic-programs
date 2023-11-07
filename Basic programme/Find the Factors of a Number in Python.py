# Find the Factors of a Number in Python :

def fun(n):
    i = 1
    while i <= n:
        if n % i == 0:
            print(i,end= "  ")
        i += 1




n = int(input("Enter a number : "))
print ("The divisors of ",n," are: " ,end="")
fun(n)
