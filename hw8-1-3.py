# Author: IBN (AMDG) 12/6/2021

def areacalc(length, width):
    area = length * width
    return area


length = int(input("What was the length? "))
width = int(input("What was the width? "))
print(areacalc(length, width))

print(areacalc(5, 4) == 20)
print(areacalc(6, 3) == 18)
print(areacalc(10, 4) == 40)
