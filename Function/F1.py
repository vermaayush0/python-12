def Area_of_Rect(l,b):
    return l*b
def Peri_of_Rect(l,b):
    return 2+(l+b)

length=int(input("Enter the value of length :"))
breadth=int(input("Enter the value of breadth :"))
area = Area_of_Rect(length,breadth)
perimeter = Peri_of_Rect(length,breadth)
print(f'Area of rectangle is {area}')
print(f'Perimeter of rectangle is {perimeter}')

