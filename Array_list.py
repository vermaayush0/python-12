# Largest integer value in a given array
'''
ls = []
while 1:
    item = int(input("Enter integer : "))
    if item == "":
        break
    ls.append(item)

ls.sort()
print("Largest element is:", ls[-1])
'''


num = input("Enter the number : ").split()

ls = [int (i) for i in num]
reg = []

for i in ls:
    if i not in reg :
        reg.append(i)
maxls = max(reg)
reg.remove(maxls)

maxls1 = max(reg)
print(maxls1)