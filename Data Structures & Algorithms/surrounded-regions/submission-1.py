class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r,c):
            direcs = [[1,0],[0,1],[-1,0],[0,-1]]
            visit.add((r,c))
            board[r][c]='T'
            for di in direcs:
                nr,nc = r+di[0],c+di[1]
                visit.add((r,c))
                if ((nr,nc) not in visit) and (nr in range(ROWS)) and (nc in range(COLS)) and (board[nr][nc]=='O'):
                    dfs(nr,nc)

        for c in range(COLS):
            if board[0][c] == 'O' and (0,c) not in visit:
                dfs(0,c)
            if board[ROWS-1][c] == 'O' and (ROWS-1,c) not in visit:
                dfs(ROWS-1,c)

        for r in range(ROWS):
            if board[r][0] == 'O' and (r,0) not in visit:
                dfs(r,0)
            if board[r][COLS-1] == 'O' and (r,COLS-1) not in visit:
                dfs(r,COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


