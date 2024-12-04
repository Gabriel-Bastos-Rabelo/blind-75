#time complexity O(n)
#space complexity O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        preview = None
        first = None
        left = list1
        right = list2

        while left and right:
            if left.val < right.val:
                if preview == None:
                    preview = left
                    first = left
                    left = left.next
                else:
                    preview.next = left
                    preview = left
                    left = left.next

            else:
                if preview == None:
                    preview = right
                    first = right
                    right = right.next
                else:
                    preview.next = right
                    preview = right
                    right = right.next

        while left:
            preview.next = left
            preview = left
            left = left.next

        while right:
            preview.next = right
            preview = right
            right = right.next

        return first

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        return self.merge(list1, list2)
    


        