st = input("Enter any string : ")
vow = 0
cons = 0
dig = 0
spa = 0

for i in st :
    if st in "aeiouAEIOU":
        vow += 1
    elif i.isalpha():
        cons += 1
    elif i.isdigit():
        dig += 1
    elif i.isspace :
        spa += 1    

print("Number of vowel : ",vow)
print("Number of consonsnts : ",cons)
print("Number of digit : ",dig)
print("Number of space : ",spa)
