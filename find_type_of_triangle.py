def triangle_type(a, b, c):
  # Check if the triangle is valid
  if a + b <= c or b + c <= a or c + a <= b:
    return "Invalid"
  # Check if the triangle is right angled
  if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    return "Right angled"
  # Check if the triangle is isosceles
  if a==b or b==c or c==a :
    return "Isosceles"
  # Otherwise, the triangle is scalene
  return "Scalene"
# Get the sides of the triangle from the user
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
# Print the type of the triangle
print(triangle_type(a, b, c))