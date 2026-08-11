from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append([i,j])
                elif grid[i][j]==1:
                    fresh += 1
        direcs = [[-1,0],[1,0],[0,-1],[0,1]]
        time = 0
        while q and fresh > 0:
            time+=1
            for _ in range(len(q)):
                [x, y] = q.popleft()
                for direc in direcs:
                    nx, ny = x+direc[0], y+direc[1]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]==1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))

        return time if fresh == 0 else -1