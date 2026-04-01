class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            visit = set()
            q.append((r,c))
            dist = 0

            while q:
                r,c = q.popleft()
                direc = [[1,0],[0,1],[-1,0],[0,-1]]
                for di in direc:
                    nr,nc = r+di[0],c+di[1]
                    if (nr,nc) not in visit and nr in range(ROWS) and nc in range(COLS) and grid[nr][nc]!=-1:
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        if grid[nr][nc]!=0:
                            grid[nr][nc]=min(grid[nr][nc],grid[r][c]+1)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    bfs(r,c)