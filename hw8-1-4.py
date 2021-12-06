# Author: IBN (AMDG) 12/6/2021
def temperature(fahrenheit):
    celcius = ((fahrenheit) - 32) * (5 / 9)
    return celcius


fahrenheit = int(input("What is your Fahrenheit temperautre? "))
print(temperature(fahrenheit))

print(temperature(32) == 0)
print(temperature(56) == 13.333333333333334)
print(temperature(100) == 37.77777777777778)
