x=int(input("Choose a number and I will tell if it's prime"))

for i in range (2,x-1):
    if x % i == 0:
        y=1
        break
    else:
        y=0
if y == 0:
    print("Prime Number")
    
else:
    print("Not a Prime Number")
