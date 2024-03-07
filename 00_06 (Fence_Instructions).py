
print("The cost of one meter is equal to... ")
metre = float(input("How much do you want one meter to cost? "))

width = float(input("Width: "))
height = float(input("Height: "))

area = width * height
perimeter = 2 * (width + height)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print(f"Cost (Perimeter * ${metre}): ${perimeter * metre}")
