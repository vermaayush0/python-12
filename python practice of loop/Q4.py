num = int(input("Enter any integer :"))
i = 1
s = 0

while i <=num:
    if i%2==0:
        s = s + i
    i = i + 1
print("Sum of even number",s)