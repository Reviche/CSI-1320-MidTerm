int1 = int(input("Enter a number: "))
int2 = int(input("Enter a number: "))
int3 = int(input("Enter a number: "))
int4 = int(input("Enter a number: "))
intlist = [int1,int2,int3,int4]
intlistP =[]
intlistN = []
if int1 >= 0:
    intlistP.extend([int1])
else:
    intlistN.extend([int1])
    
if int2 >= 0:
    intlistP.extend([int2])
else:
    intlistN.extend([int2])
    
if int3 >= 0:
    intlistP.extend([int3])
else:
    intlistN.extend([int3])
    
if int4 >= 0:
    intlistP.extend([int4])
else:
    intlistN.extend([int4])


print(intlist)
print(intlistP)
print(intlistN)
