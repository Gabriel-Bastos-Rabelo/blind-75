def alienOrder(words):
    adj = {}

    for word in words:
        for c in word:
            adj[c] = set()

    
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        minLen = min(len(word1), len(word2))

        for j in range(minLen):
            if word1[j] != word2[j]:
                adj[word1[j]].add(word2[j])
                break

    #False = visited, True = current path
    visit = {}
    res = []

    def dfs(c):
        if c in visit:
            return visit[c]
        
        visit[c] = True
        for nei in adj[c]:
            if dfs(nei):
                return True
            
        visit[c] = False
        res.append(c)


    for c in adj:
        if dfs(c):
            return ""

    res = res[::-1]
    return "".join(res)



print(alienOrder([
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
))



        