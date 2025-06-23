from collections import defaultdict

class Solution: 
  def validTree(self, n, edges):
    if len(edges) !=n-1:
      return False
    
    graph = defaultdict(list)
    print(f"Initial graph: {graph}")
    for u, v in edges:
      graph[u].append(v)
      graph[v].append(u)
      print(f"Added edge {u}-{v}, graph now:" + str(graph))

    visited = set()
    print(f"Initial visited set: {visited}")

    def dfs(node, parent):
      if node in visited:
        return False
      visited.add(node)

      for neighbor in graph[node]:
        if neighbor != parent:
          print(f"Visiting neighbor {neighbor} of node {node}")
          if not dfs(neighbor, node):
            return False
      return True
    
    if not dfs(0, -1):
      print("Cycle detected or disconnected component found.")
      return False
    print(f"Visited nodes after DFS: {visited}")
    return len(visited)==n
# Example usage:  
# n = number of nodes, edges = list of edges
# n=5
# edges=[[0,1],[0,2],[0,3],[1,4]]
# result = Solution()
# valid_tree=result.validTree(n, edges)





n=5
edges=[[0,1],[0,2],[0,3],[1,4]]
result = Solution()
valid_tree=result.validTree(n, edges)