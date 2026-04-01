"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        count = 0
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        i = 0
        j = 0
        n = len(intervals)

        start.sort()
        end.sort()
        max_count = 0
        while i<n:
            if start[i]<end[j]:
                count+=1
                i+=1
                
            else:
                count-=1
                j+=1
            max_count = max(count,max_count)
        return max_count