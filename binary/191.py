#time complexity O()

def hammingWeight(self, n: int) -> int:
    res = 0
    potence = 0
    while 2 ** potence <= n:
        if n & 1 << potence:
            res += 1
        potence += 1

    print(res)
    return res


#second solution
#time complexity O(1)
#space complexity O(1)

#11 = 1011

# 1011 & 01 = 1
# 1011 & 10 = 10
# 1011 & 100 = 0
# 1011 & 1000 = 1000
def hammingWeight(self, n: int) -> int:
    res = 0

    for i in range(32):
        if (n >> i) & 1:
            res += 1

    return res