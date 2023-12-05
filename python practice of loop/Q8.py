num = int(input("Enter any integer : "))
s = 0 
cp = num

while num!= 0:
    r = num % 10
    s = s * 10 + r 
    num = num // 10

if s == cp:
    print("Falindrome Number")
else:
    print("Not a Falindrome Number")