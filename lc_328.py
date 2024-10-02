# 328. Odd Even Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional
from list_template import ListNode, create_list_from_array, is_list_equal


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = odd_head = head
        even = even_head = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head

        return odd_head


result = Solution()
input_list = [1, 2, 3, 4, 5]
head = create_list_from_array(input_list)
output = result.oddEvenList(head)
print(f"Output: {output}")
expected = [1, 3, 5, 2, 4]
if is_list_equal(output, expected):
    print("Test passed successfully!")
else:
    print("Test failed!")
