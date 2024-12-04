#first solution
#time complexity O(nlogn)
#space complexity O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = []
        for i in lists:
            cur = i
            while cur:
                newList.append(cur.val)
                cur = cur.next
        newList.sort()
        print(newList)
        if len(newList) == 0:
            return None
        node = ListNode(newList[0])
        cur = node
        for i in range(1, len(newList)):
            cur.next = ListNode(newList[i])
            cur = cur.next
        return node


#second sulution
#time complexity O(nlogn)
#space complexity O()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right):
        initial = ListNode()
        p = initial

        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left or right
        return initial.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)


#thirt solution
#time complexity O(n log k)
#space complexity O(k)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.value < other.value  # Break tie by value
        return self.priority < other.priority

import heapq
class Solution:
    def merge(self, left, right):
        initial = ListNode()
        p = initial

        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left or right
        return initial.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, id(node), node))

        initial = ListNode(0)
        p = initial
        while pq:
            _, _, node = heapq.heappop(pq)
            p.next = node
            p = p.next

            if p.next != None:
                heapq.heappush(pq, (p.next.val, id(p.next), p.next))

        return initial.next






