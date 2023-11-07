# Check Whether or Not the Number is a Perfect Number in Python:

n = int(input("Enter a number : "))
s = 0

for i in  range(1,n):
    if n %  i == 0:
         s += i
   

if s == n :
    print("its a perfect number")
else:
    print("its not perfect number")
