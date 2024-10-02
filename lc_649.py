# 649. Dota2 Senate


from collections import deque, Counter


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        last_index = len(senate)

        for i, senator in enumerate(senate):
            if senator == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            last_index += 1
            if r_queue[0] < d_queue[0]:
                r_queue.append(last_index)
            else:
                d_queue.append(last_index)
            d_queue.popleft()
            r_queue.popleft()

        if r_queue:
            return "Radiant"
        return "Dire"


result = Solution()
senate = "RD"
output = result.predictPartyVictory(senate)
print(f"Output: {output}")
expected = "Radiant"
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
