#time complexity O(n log n)

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        pq = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for key in freq:
            heapq.heappush(pq, (-freq[key], key))

        i = 0
        ans = []
        while pq and i < k:
            freq, value = heapq.heappop(pq)
            ans.append(value)
            i += 1

        return ans

#time complexity O(n)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for key in freq:
            frequency = freq[key]
            buckets[frequency].append(key)

        res = []
        print(buckets)
        for i in range(len(buckets)-1, -1, -1):
            if len(res) >= k:
                break
            if len(buckets[i]) > 0:
                res.extend(buckets[i])

        return res




        


        