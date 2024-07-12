# 141. Linked List Cycle

class Solution(object):
    def hasCycle(self, head):
        slow = head 
        fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False