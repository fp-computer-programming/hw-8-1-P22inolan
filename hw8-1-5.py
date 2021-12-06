# Author: IBN (AMDG) 12/6/2021

def wincalc(total1, total2):
    total1 = (win1 * 3) + (draw1 * 1)
    total2 = (win2 * 3) + (draw2 * 1)

win1 = input("How many wins did Team 1 have? ")
draw1 = input("How many draws did Team 1 have? ")
win2 = input("How many wins did Team 2 have? ")
draw2 = input("How many draws did Team 2 have? ")

total1 = (int(win1) * 3) + (int(draw1) * 1)
total2 = (int(win2) * 3) + (int(draw2) * 1)

if total1 > total2:
    print("Team 1 had more points.")
else:
    print("Team 2 had more points.")