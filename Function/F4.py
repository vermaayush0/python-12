def Vote(Age):
    return Age>=18 
age = int(input("Enter a Age : "))
if Vote(age):
    print("Yes")
else :
    print("No")