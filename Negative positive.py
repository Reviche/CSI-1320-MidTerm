#Exam-Q4: Write a program that takes four numbers as input and add these numbers into a list. 
# This number could be positive, negative and zero. After that,

#1) You need to separate negative and positive numbers in two different lists

#2) Also, your program should be able to count the number of zero in the input data set

#3) You need to print all the results on the screen (original data set that user inputs, 
# the data set contains only negative numbers, 
# the list of positive numbers, and also the number of zero in the data set).




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
