from collections import defaultdict, deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        adj = defaultdict(list)
        indegree = [0] * n
        
        # Step 1: Build adjacency list and compute in-degrees
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        # Step 2: Initialize color count for each node
        count = [[0] * 26 for _ in range(n)]  # 26 lowercase English letters
        
        # Step 3: Queue for topological sort (nodes with in-degree 0)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                color_index = ord(colors[i]) - ord('a')
                count[i][color_index] = 1  # Initial color count
        
        # Step 4: Topological sort with color count tracking
        visited = 0
        res = 0
        
        while queue:
            node = queue.popleft()
            visited += 1
            res = max(res, max(count[node]))  # Update result
            
            for neighbor in adj[node]:
                for c in range(26):
                    current_color = ord(colors[neighbor]) - ord('a')
                    # Update the color count for the neighbor
                    count[neighbor][c] = max(
                        count[neighbor][c],
                        count[node][c] + (1 if c == current_color else 0)
                    )
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 5: Check for cycle
        return res if visited == n else -1
