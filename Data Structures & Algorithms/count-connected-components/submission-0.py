class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = self.adj_list(edges,n)
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count+=1
                self.explore(graph,i,visited)
        
        return count


    def adj_list(self, edges, n):
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        return graph
    
    def explore(self, graph, src, visited):
        if src in visited:
            return False
        visited.add(src)

        for neighbours in graph[src]:
            self.explore(graph, neighbours, visited)