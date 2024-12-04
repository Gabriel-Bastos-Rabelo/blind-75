#time complexity O(n)
#space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            current = head.next
            head.next = None
            previous = head
            while current:
                nextElement = current.next
                current.next = previous
                previous = current
                current = nextElement

    
            return previous

        return None

            

           

