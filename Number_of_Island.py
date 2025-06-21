class Solution: 
  def numIslands(self, grid):
    if not grid:
      return 0
    rows, cols = len(grid), len(grid)
    count = 0

    def dfs(r, c):
      if r < 0 or r >= rows or c < 0 or c >=cols or grid[r][c] != '1':
        return 
      grid [r][c] = '0'
      dfs(r+1,c)
      dfs(r-1,c)
      dfs(r,c+1)
      dfs(r,c-1)
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == '1':
          count += 1
          dfs(r, c)
          print(f"Island found, incrementing count to {count}")
          
grid= [["1","1","1","1","0"],
       ["1","0","0","1","0"],
       ["1","0","0","0","0"],
       ["0","0","0","1","0"],
       ["1","1","1","1","1"]]
s=Solution()
s.numIslands(grid)
