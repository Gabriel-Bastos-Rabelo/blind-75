#time complexity O(n)
#space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        numberElements = 0
        cur = head

        while cur:
            numberElements += 1
            cur = cur.next

        if n == numberElements:
            head = head.next

        else:
            cur = head
            previous = ListNode()
            i = 0
            while (numberElements - i) > n:
                previous = cur
                cur = cur.next
                i += 1

            previous.next = cur.next

        return head
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = head

        i = 0
        fast = head
        while i < n:
            fast = fast.next
            i += 1

        previous = None
        while fast:
            fast = fast.next
            previous = slow
            slow = slow.next

        if not previous:
            return head.next
        previous.next = slow.next
        return head


