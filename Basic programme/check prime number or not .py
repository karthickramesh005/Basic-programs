# prime number ort not ;.

num = int(input("enter a number :  "))

f = 0

for i in range (2,num):
    if num % i == 0 :
        f = 1
        break
if f == 0:
    print("This is prime number")
else :
    print("This is not prime number")
