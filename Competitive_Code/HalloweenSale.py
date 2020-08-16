#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    total = 0
    flag = False
    while(p>m):
        if s-p>=0:
            s-=p
            p-=d
            total+=1
        else:
            flag=True
            break
    if flag==False:
        while(s-m>=0):
            s-=m
            total+=1
    return total

if __name__ == '__main__':

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    print (answer)
