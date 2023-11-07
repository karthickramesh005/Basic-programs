# print prime numbers between two numbers :

st = int(input("Enter a start number : "))
ed = int(input("Enter a end number : "))
li = []

for i in range(st,ed+1):
    f = 0
    
    if i < 2 :
        continue
    
    if i == 2:
        li.append(2)
        continue

    for x in range (2,i):
        if i % xs == 0:
            f = 1
            break
    if f == 0:
        li.append(i)

print(li)
