class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        res = [intervals[0]]
        for start, end in intervals:
            last_end = res[-1][1]
            if start>last_end:
                res.append([start,end])
            else:
                res[-1][1]=max(end,last_end)

        return res