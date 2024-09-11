class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visit = set()
        R, C = len(grid), len(grid[0])
        count = 0
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(row, col):
            for dr, dc in direction:
                r, c = row + dr, col + dc
                
                if (0 <= r < R) and (0 <= c < C) and (r,c) not in visit and grid[r][c] == "1":
                    visit.add((r, c))
                    dfs(r, c)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    count += 1
        return count
        