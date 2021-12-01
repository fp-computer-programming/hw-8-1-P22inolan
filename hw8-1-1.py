# Author: IBN (AMDG) 11/29/2021


def score(frees, twos, threes):
    points = int(frees) + (int(twos) * 2) + (int(threes) * 3)
    return points


tally1 = input("How many free throws were made? ")
tally2 = input("How many twos were made? ")
tally3 = input("How many threes were made? ")

print(score(tally1, tally2, tally3))

print(score(1, 1, 1) == 6)
print(score(3, 6, 2) == 21)
print(score(8, 10, 7) == 49)
