from functools import reduce

N = int(input())
x = list(map(int, input().rstrip().split()))
w = list(map(int, input().rstrip().split()))

# N = 3
# x = [1, 2, 3]
# w = [1, 1, 1]

mean = 0

for z in list(zip(x, w)):
    mean += z[0] * z[1]
mean = 0
for i in range(N):
    mean += x[i] * w[i]

mean /= sum(w)

print("{0:.1f}".format(mean))
