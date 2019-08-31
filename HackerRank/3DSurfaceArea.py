#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A,H,W):
    row,col = H,W
    surfaceArea = 0
    addedRow = [0 for x in range(col)]
    A.insert(0,addedRow)
    A.append(addedRow)
    for i in range(row+2):
        A[i] = [0] + A[i] + [0]
    for i in range(1,row+1):
        for j in range(1,col+1):
            surfaceArea+=2
            if(A[i][j]-A[i][j-1]>0):
                surfaceArea+=A[i][j]-A[i][j-1]
            if(A[i][j]-A[i-1][j]>0):
                surfaceArea+=A[i][j]-A[i-1][j]
            if(A[i][j]-A[i+1][j]>0):
                surfaceArea+=A[i][j]-A[i+1][j]
            if(A[i][j]-A[i][j+1]>0):
                surfaceArea+=A[i][j]-A[i][j+1]
    return surfaceArea

if __name__ == '__main__':

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A, H, W)
    print (result)
