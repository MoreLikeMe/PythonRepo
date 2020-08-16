#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    l = []
    flag = True
    count = 0
    if k==0:
        return [x for x in range(1,n+1)]
    if n%k!=0 or (n%k==0 and (n//k)%2==1):
        return [-1]
    for i in range(n):
        if flag==True:
            l.append(i+1+k)
        else:
            l.append(i+1-k)
        count+=1
        if count==k:
            count = 0
            flag = not flag
    return l

if __name__ == '__main__':


    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print (result)
