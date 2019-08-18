
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    index = 0
    while(index < len(c) - 1):
        if (index + 2 <= len(c) - 1) and (c[index + 2] == 0):
            index = index + 2
        else:
            index +=1
        jumps += 1
    return jumps
