#time complexity O(n)
#space complexity O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        visited = set()
        visited.add(head)

        while current:
            current = current.next
            if current in visited:
                return True

            if current:
                visited.add(current)

        return False
    
#time complexity O(n)
#space complexity O(1)
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #If two points are moving circularly with different velocities, then they will always meet at some point in time.

        walker = head
        runner = head

        while walker and walker.next and runner and runner.next and runner.next.next:
            walker = walker.next
            runner = runner.next.next

            if walker == runner:
                return True

        return False