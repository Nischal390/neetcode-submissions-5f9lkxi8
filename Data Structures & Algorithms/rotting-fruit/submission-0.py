class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        q = deque()
        direcs = [[1,0],[0,1],[-1,0],[0,-1]]
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
            
        while q and fresh>0:
            Qlen = len(q)
            for i in range(Qlen):
                r,c = q.popleft()
                for di in direcs:
                    nr = r + di[0]
                    nc = c + di[1]
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]==1:
                        fresh-=1
                        q.append((nr,nc))
                        grid[nr][nc] = 2
            minutes+=1
                

        if fresh == 0:
            return minutes

        return -1