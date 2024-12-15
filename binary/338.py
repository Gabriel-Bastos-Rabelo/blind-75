#this works because the number of bits of a odd number will be the previous even one plus de bit 1, and as we know that to double a number is only shiftted 1 to the right that is add a 0 in the begenning, the number of bits for a even number is the number of bits of this number divided by 2 

def countBits(self, n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(1, n+1):
        if i % 2 == 0:
            ans[i] = ans[i//2]
        else:
            ans[i] = ans[i-1] + 1

    return ans