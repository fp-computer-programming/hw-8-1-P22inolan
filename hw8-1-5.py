# Author: IBN (AMDG) 12/6/2021

def wincalc(win1, draw1, win2, draw2):
    total1 = (int(win1) * 3) + int(draw1)
    total2 = (int(win2)* 3) + int(draw2)
    if total1 > total2:
        return "Team 1 had more points. "
    else:
        return "Team 2 had more points. "


win1 = input("How many wins did Team 1 have? ")
draw1 = input("How many draws did Team 1 have? ")
win2 = input("How many wins did Team 2 have? ")
draw2 = input("How many draws did Team 2 have? ")

wincalc(win1, draw1, win2, draw2)

print(wincalc(10, 0 ,5 ,5) == "Team 1 had more points. ")
print(wincalc(4, 5, 5, 4) == "Team 2 had more points. ")
print(wincalc(10, 2, 8, 3) == "Team 1 had more points. ")
