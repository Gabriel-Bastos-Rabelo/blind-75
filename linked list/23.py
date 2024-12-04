#time complexity O(n log k)
#space complexity O(log k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, left, right, lists):
        
        if right-left == 0:
            return lists[left]


        
        mid = left + ((right - left)//2)
        
        l = self.merge(left, mid, lists)
        r = self.merge(mid+1, right, lists)

        #merge

        initial = ListNode()
        current = initial
        while l and r:
            if l.val < r.val:
                current.next = l
                current = l
                l = l.next
            else:
                current.next = r
                current = r
                r = r.next

        while l:
            current.next = l
            current = l
            l = l.next

        while r:
            current.next = r
            current = r
            r = r.next

        return initial.next


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    left = 0
    right = len(lists)-1
    print(lists)
    return self.merge(left, right, lists)
    

def heapSolution(self, lists):
        hp = []

        for node in lists:
            if node:
                heapq.heappush(hp, (node.val, id(node), node))

        if not hp:
            return None
        value, ident, initial = heapq.heappop(hp)

        if initial.next:
            heapq.heappush(hp, (initial.next.val, id(initial.next), initial.next))
        
        current = initial

        while hp:
            value, ident, elm = heapq.heappop(hp)
            current.next = elm
            current = current.next
            if elm.next:
                heapq.heappush(hp, (elm.next.val, id(elm.next), elm.next))

        return initial



def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return self.heapSolution(lists)