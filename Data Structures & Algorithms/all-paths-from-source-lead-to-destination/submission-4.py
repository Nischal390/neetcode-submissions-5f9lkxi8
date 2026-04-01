#         1
#       / | \    
#      2- 3- 4
#     /
#    5 


"""

visited = {
    3, 0
}

"""

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            visited.add(node)
            path.append(node)
            for adjNode in reverseGraph[node]:
                if(adjNode in path):
                    return False
                if dfs(adjNode) == False:
                    return False
            path.pop()
            return True
        def rec(node):
            if(node not in visited):
                return False
            for adjNode in originalGraph[node]:
                if rec(adjNode) == False:
                    return False
            return True
        reverseGraph = [[] for _ in range(n)]
        originalGraph = [[] for _ in range(n)]
        for edge in edges:
            reverseGraph[edge[1]].append(edge[0])
            originalGraph[edge[0]].append(edge[1])
        print(reverseGraph)
        print(originalGraph)
        path = []
        visited = set()
        if dfs(destination) == False:
            return False
        print("Hello")
        return rec(source)
        
        
        



