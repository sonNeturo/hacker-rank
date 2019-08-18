
N = int(input())
arr = list(map(int, input().rstrip().split()))

# Mean
mean = sum(arr)/len(arr)

# median
srt = sorted(arr)
if len(arr) % 2 == 1:
    median = srt[len(arr)//2]
else:
    median = (srt[len(arr)//2] + srt[len(arr)//2 - 1])/2

print("{0:.1f}".format(mean))
print("{0:.1f}".format(median))

count_dic = {i: 0 for i in arr}
for i in arr:
    count_dic[i] += 1
max_count = 0
vals = []
for k, v in count_dic.items():
    if v > max_count:
        vals = [k]
        max_count = v
    elif v == max_count:
        vals.append(k)
print(min(vals))
