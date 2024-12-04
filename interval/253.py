intervals = [[0, 30],[5, 10],[15, 20]]

intervals.sort(key = lambda x: x[1])

start = []
end = []
for i in intervals:
    start.append(i[0])
    end.append(i[1])

start.sort()


p1 = 0
p2 = 0

ans = 0
count = 0
while p1 < len(start):
    if start[p1] <= end[p2]:
        p1 += 1
        count += 1

    else:
        count -= 1
        p2 += 1

    ans = max(ans, count)


print(ans)
