#WAPP print repeted string
st = input("Enter any string : ")
reg = " "
for i in st:
    if i not in reg and st.count(i)>=2:
        reg += i
print(reg)