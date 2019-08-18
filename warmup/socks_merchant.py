#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dic = dict()
    for i in ar:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    n_valid_pairs = 0
    for k, v in dic.items():
        n_valid_pairs += math.floor(v / 2)
    return n_valid_pairs




