# Author: IBN (AMDG) 11/29/2021


def score(frees, twos, threes):
    points = frees + (twos * 2) + (threes * 3)
    return "The player scored " + points + " points in the game."


print(score(1, 1, 1) )