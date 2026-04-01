class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        q = deque()
        visit = set()

        def bfs(r,c):
            q.append((r,c))
            visit.add((r,c))
            while q:
                r,c = q.pop()
                for dr,dc in directions:
                    nr, nc = r+dr,c+dc
                    if nr<ROWS and nr>=0 and nc<COLS and nc>=0 and grid[nr][nc]=='1' and ((nr,nc) not in visit):
                        visit.add((nr,nc))
                        q.append((nr,nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and (r,c) not in visit:
                    bfs(r,c)
                    islands+=1

        return islands