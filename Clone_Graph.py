class Node:
  def __init__(self, val=0, neighbors=None):
    self.val =val
    self.neighbors = neighbors if neighbors is not None else []

class Solution: 
  def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
      return None
    
    old_to_new = {}
    
    def dfs(node):
      if node in old_to_new:
        return old_to_new[node]
      
      copy = Node(node.val)
      old_to_new[node] = copy
      
      for neighbor in node.neighbors:
        copy.neighbors.append(dfs(neighbor))
      
      return copy
    
    return dfs(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]


print(node1.val)  # Output: 1
print(node1.neighbors[0].val)  # Output: 2

solution = Solution()
cloned_graph = solution.cloneGraph(node1)

