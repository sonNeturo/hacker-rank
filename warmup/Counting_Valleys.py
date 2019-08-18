#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    valley_count = 0

    for i in s:
        level_prev = level
        level_new = level + (1 if i == 'U' else -1)
        if level_prev == 0 and level_new < 0:
            valley_count += 1
        level = level_new
    return valley_count - 1 if(level_new < 0) else valley_count

