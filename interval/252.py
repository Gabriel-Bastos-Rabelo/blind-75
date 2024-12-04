intervals = [[7,10],[2,4]]
intervals.sort(key = lambda x: x[1])

ans = True

for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i-1][1]:
        ans = False
        break


print(ans)