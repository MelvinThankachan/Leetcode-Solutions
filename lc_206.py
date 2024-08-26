# 206. Reverse Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional
from list_template import ListNode, create_list_from_array, is_list_equal


# My solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        stack = []
        while head is not None:
            stack.append(head)
            head = head.next

        result_head = stack.pop()
        head = result_head
        while stack:
            head.next = stack.pop()
            head = head.next
        head.next = None

        return result_head


# Best solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        return prev_node


result = Solution()
arr = [1, 2, 3, 4, 5]
head = create_list_from_array(arr)
output = result.reverseList(head)
print("output", output)
expected = [5, 4, 3, 2, 1]
if is_list_equal(output, expected):
    print("Test passed successfully!")
