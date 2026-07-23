import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = [point[0]**2+point[1]**2]
            dist.append(point[0])
            dist.append(point[1])
            heap.append(dist)
        
        heapq.heapify(heap)

        res = []
        for i in range(k):
            ele = heapq.heappop(heap)
            res.append(ele)
        

        return [[point_s[1],point_s[2]] for point_s in res]