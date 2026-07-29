from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req_map = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            pre_req_map[crs].append(pre)

        course_visited = set()
        def dfs(crs):
            if crs in course_visited:
                return False
            if pre_req_map[crs]==[]:
                return True
            course_visited.add(crs)
            for c in pre_req_map[crs]:
                if not dfs(c):
                    return False
            course_visited.remove(crs)
            pre_req_map[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True