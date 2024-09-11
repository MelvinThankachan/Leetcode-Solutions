# 877. Stone Game

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alice = 0
        bob = 0
        alice_turn = True
        left_pointer = 0
        right_pointer = len(piles) - 1

        while left_pointer < right_pointer:
            first_pile = piles[left_pointer]
            last_pile = piles[right_pointer]
            pile = None
            if first_pile > last_pile:
                pile = first_pile
                left_pointer += 1
            else:
                pile = last_pile
                right_pointer -= 1

            if alice_turn:
                alice += pile
            else:
                bob += pile

            alice_turn = not alice_turn

        return alice > bob


result = Solution()
piles = [3, 2, 10, 4]
output = result.stoneGame(piles)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")

