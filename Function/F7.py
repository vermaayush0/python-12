def Factor(f):
    a = []
    for i in range (1,f):
        if (f%i==0):
            a.append(i)
    return a
n= int(input("Enter the number : "))
out = Factor(n)
print(out)
''' 
Write a python function that recive list of integer and return 1 if all the int value are sorted in accending order else return -1

'''
