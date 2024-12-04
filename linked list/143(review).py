#time complexity O(n)
#space complexity O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self, head):
        
        current = head
        previous = None
        nextElm = None

        while current:
            nextElm = current.next
            current.next = previous
            previous = current
            current = nextElm


        return previous
    

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return 
        slow = head
        faster = head
        previous = None
        while faster and faster.next:
            previous = slow
            slow = slow.next
            faster = faster.next.next

        previous.next = None
        left = head
        right = self.reverse(slow)
        previous = None


        while left and right:
            if previous:
                previous.next = left

            nextLeft = left.next
            left.next = right
            left = nextLeft
            previous = right
            right = right.next
        
        



        

#cleaner
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        prev, curr = None, slow.next


        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt



        slow.next = None

        head1, head2 = head, prev

        while head1 and head2:
            nextt = head1.next
            nextt2 = head2.next

            head1.next = head2
            head1 = nextt

            head2.next = head1
            head2 = nextt2




