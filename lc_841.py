# 841. Keys and Rooms


from typing import List
from collections import deque


class Solution:
    # Depth-First Search Solution
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_seen = [False for _ in rooms]
        rooms_seen[0] = True
        n = len(rooms)
        count = 1

        def dfs(node):
            room = rooms[node]
            for key in room:
                if not rooms_seen[key]:
                    rooms_seen[key] = True
                    nonlocal count
                    count += 1
                    dfs(key)

        dfs(0)
        return count == n

    # Breadth-First Search Solution
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_seen = [False for _ in rooms]
        queue = deque([0])
        rooms_seen[0] = True
        n = len(rooms)
        count = 1

        while queue:
            room = rooms[queue.popleft()]
            for key in room:
                if not rooms_seen[key]:
                    queue.append(key)
                    rooms_seen[key] = True
                    count += 1

        return count == n


result = Solution()
rooms = [[1], [2], [3], []]
output = result.canVisitAllRooms(rooms)
print(f"Output: {output}")
expected = True
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
