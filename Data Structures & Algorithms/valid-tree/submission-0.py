class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        # adj_map = {i:[] for i in range(n)}
        adj_map = collections.defaultdict(list)
        # undirected graph map
        for u,v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)
        # def has_cycle(node,parent,visited,adj_map):
            # visited.add(node)
            # for neighbor in adj_map[node]:
            #     # if neighbor == parent:
            #     #     continue
            #     if neighbor in visited and neighbor != parent:
            #         return True #cycle detected
            #     if has_cycle(neighbor,node,visited,adj_map):
            #         return True
            # return False  

        visited = set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in adj_map[node]:
                dfs(neighbor)
        
        dfs(0)
        return len(visited) == n # we can reach all nodes
            
