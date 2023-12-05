st = input("Enter any string : ")
reg = " "
for i in st:
    if i not in reg:
        print(f"{i}: {st.count(i)}")
        reg += i