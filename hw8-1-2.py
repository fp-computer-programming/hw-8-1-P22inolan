# Author: IBN (AMDG) 12/6/2021
def circlearea(radius):
    area = 3.14 * (radius ** 2)
    return area


rad = int(input("What was the radius of the circle? "))
print(circlearea(rad))

print(circlearea(4.6) == 66.44239999999999)
print(circlearea(21) == 1384.74)
print(circlearea(5) == 78.5)
