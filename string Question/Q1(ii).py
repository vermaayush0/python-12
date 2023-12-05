# WAPP to remove dublicate string
st = input("Enter any string : ")
reg = " "
for i in st:
    if i not in  reg:
        reg += i
print(reg)
