class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        self.area = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit = set()

        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            cur_area = 1
            while q:
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r+dr,c+dc
                    if nr<ROWS and nr>=0 and nc<COLS and nc>=0 and grid[nr][nc]== 1 and ((nr,nc) not in visit):
                        visit.add((nr,nc))
                        q.append((nr,nc))
                        cur_area+=1
                self.area = max(self.area, cur_area)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1 and (r,c) not in visit:
                    bfs(r,c)   

        return self.area