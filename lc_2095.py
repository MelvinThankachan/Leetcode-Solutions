# 2095. Delete the Middle Node of a Linked List


from typing import Optional
from list_template import ListNode, create_list_from_array, is_list_equal


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # Using Floyd's slow-fast pointer approach
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        current_node = None
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            current_node = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        current_node.next = slow_pointer.next

        return head


result = Solution()
input_list = [1, 3, 4, 7, 1, 2, 6]
head = create_list_from_array(input_list)
output = result.deleteMiddle(head)
print(f"Output: {output}")
expected = [1, 3, 4, 1, 2, 6]
if is_list_equal(output, expected):
    print("Test passed successfully!")
else:
    print("Test failed!")
