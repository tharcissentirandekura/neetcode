class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # 
        graph = {}

        for source, destination in edges:
            graph.setdefault(source, []).append(destination)
            graph.setdefault(destination, []).append(source)

        print(graph)
        visited = set()
        def bfs(node):
            q = deque([node])
            visited.add(node)
            while q:
                curr = q.popleft()
                for neighbor in graph.get(curr, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)


        count = 0
        # components is number of dfs initialized
        for node in range(n):
            if node not in visited:
                bfs(node)
                count += 1

        return count
                    





