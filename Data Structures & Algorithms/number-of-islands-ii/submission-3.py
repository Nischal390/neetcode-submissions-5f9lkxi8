class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        grid = [[0] * n for _ in range(m)]
        components = 0
        def union(cord1, cord2):
            nonlocal components
            p1 = find(cord1)
            p2 = find(cord2)
            if p1 != p2:
                parent[p1] = p2
                return True
            return False
        def find(cord):
            if parent[cord] == cord:
                return cord
            parent[cord] = find(parent[cord])
            return parent[cord]
        result = []
        for position in positions:
            i,j = position
            if grid[i][j] == 1:
                result.append(components)
                continue
            grid[i][j] = 1
            parent[(i,j)] = (i,j)
            components+=1
            for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                ni,nj = di + i, dj + j
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    if union((ni,nj),(i,j)):
                        components-=1
            result.append(components)
        return result
            