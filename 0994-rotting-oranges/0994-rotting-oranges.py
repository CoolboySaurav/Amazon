class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        q = deque()
        good_orange = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    good_orange += 1
                elif grid[i][j] == 2:
                    q.append([i,j])
        time = 0
        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        while q and good_orange > 0:
            L = len(q)
            
            for i in range(L):
                row, col = q.popleft()
                
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        good_orange -= 1
                        grid[r][c] = 2
                        q.append([r, c])
            time += 1
        
        return time if not good_orange else -1
                
            