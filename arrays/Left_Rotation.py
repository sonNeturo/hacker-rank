import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    rot = d % len(a)
    res = a.copy()
    res[:len(a)-rot] = a[rot:len(a)]
    res[len(a)-rot:] = a[:rot]
    return res
