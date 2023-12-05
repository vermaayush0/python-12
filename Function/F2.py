def Area_of_Circle(r):
    return 3.14*r**2
def Circumference_of_Circle(r):
    return 2*3.14*r

radius=int(input("Enter the value of Radius :"))
area = Area_of_Circle(radius)
circumference = Circumference_of_Circle(radius)
print(f'Area of circle is {area}')
print(f'Perimeter of circle is {circumference}')

