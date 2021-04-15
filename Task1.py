# Calculate the side of a triangle
ab = input("Please enter ab: ")
bc = input("please enter bc: ")

ac = (int(ab)**2 + int(bc)**2)**(1/2)

print("ac is: " + str(ac))

height = ab
base = bc
area = (int(height) * int(base)) / 2

print("The area of the triangle is: " + str(area))
print("The area of the triangle is: " + str(bin(int(area))))