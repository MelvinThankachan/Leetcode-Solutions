# 2130. Maximum Twin Sum of a Linked List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional
from list_template import ListNode, create_list_from_array
from collections import deque


class Solution:
    # My Solution using deque
    def pairSum(self, head: Optional[ListNode]) -> int:
        root = head
        queue = deque()

        while root is not None:
            queue.append(root)
            root = root.next

        max_pair_sum = 0
        while queue:
            max_pair_sum = max(max_pair_sum, queue.popleft().val + queue.pop().val)

        return max_pair_sum

    # My solution using array
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        values = []

        while current is not None:
            values.append(current.val)
            current = current.next

        n = len(values)
        max_sum = 0
        for i in range(n // 2):
            twin_sum = values[i] + values[n - 1 - i]
            if twin_sum > max_sum:
                max_sum = twin_sum

        return max_sum

    # Another Solution
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Finding the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the second half
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Calculating the maximum twin sum
        max_sum = 0
        first_half = head
        second_half = prev  # 'prev' is now the head of the reversed second half
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, twin_sum)
            first_half = first_half.next
            second_half = second_half.next

        return max_sum


result = Solution()
input_list = [5, 4, 2, 1]
head = create_list_from_array(input_list)
output = result.pairSum(head)
print(f"Output: {output}")
expected = 6
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
