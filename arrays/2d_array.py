import math


def hourglassSum(arr):
    max_sum = -math.inf
    for i in range(4):
        for j in range(4):
            curr_sum = 0
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if not ((l == j and k == i+1) or (l == j+2 and k == i+1)):
                        curr_sum += arr[k][l]
            if curr_sum > max_sum:
                max_sum = curr_sum
    return max_sum