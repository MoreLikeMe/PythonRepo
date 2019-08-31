#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    ball = [0 for x in range(len(container))]
    box = [0 for x in range(len(container))]
    for i in range(len(container)):
        for j in range(len(container)):
            ball[j]+=container[i][j]
            box[i]+=container[i][j]
    ball.sort()
    box.sort()
    stat = "Possible"
    for i in range(len(container)):
        if(ball[i]!=box[i]):
            stat = "Impossible"
            break
    return stat

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print (result)
