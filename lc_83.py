# 83. Remove Duplicates from Sorted List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from list_template import ListNode, create_list_from_array, is_list_equal, print_list


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_node = head

        while head is not None:
            next_node = head.next
            if next_node is None:
                break
            if next_node.val == head.val:
                head.next = next_node.next
            else:
                head = head.next

        return head_node


result = Solution()
list = [1, 1, 2]
head = create_list_from_array(list)
output = result.deleteDuplicates(head)
print(f"Output: {output}")
expected = [1, 2]
if is_list_equal(output, expected):
    print("Test passed successfully!")
else:
    print("Test failed!")
