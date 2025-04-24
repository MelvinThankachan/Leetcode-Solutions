# 1466. Reorder Routes to Make All Paths Lead to the City Zero


from typing import List
from collections import deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections_graph = [[] for _ in range(n)]
        visited_cities = [False for _ in range(n)]

        for start, end in connections:
            connections_graph[start].append(-end)
            connections_graph[end].append(start)

        result = 0
        bfs_nodes = deque([0])
        visited_cities[0] = True

        while bfs_nodes:
            current_node = bfs_nodes.popleft()

            for end_node in connections_graph[current_node]:
                if visited_cities[abs(end_node)]:
                    continue
                if end_node < 0:
                    result += 1

                visited_cities[abs(end_node)] = True
                bfs_nodes.append(abs(end_node))

        return result


result = Solution()
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
output = result.minReorder(n, connections)
print(f"Output: {output}")
expected = 3
if output == expected:
    print("Test passed successfully!")
else:
    print("Test failed!")
