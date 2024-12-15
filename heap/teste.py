
def isAnagram(stringA: str, stringB: str) -> bool:

    if len(stringA) != len(stringB):
        return False
    freq = {}
    for c in stringA:
        freq[c] = freq.get(c, 0) + 1


    for c in stringB:
        if c not in freq:
            return False
        
        else:
            freq[c] -= 1
            if freq[c] < 0:
                return False
            

    return True


    