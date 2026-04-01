class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        t, b = 0, r - 1
        while t<=b:
            r = (t+b)//2
            if target>matrix[r][-1]:
                t = r + 1
            elif target<matrix[r][0]:
                b = r - 1
            else:
                break

        if not (t<=b):
            return False

        r = (t+b)//2
        l,ri = 0, c-1
        while l<=ri:
            m = (l+ri)//2
            if target>matrix[r][m]:
                l = m+1
            elif target<matrix[r][m]:
                ri=m-1
            else:
                return True
        return False