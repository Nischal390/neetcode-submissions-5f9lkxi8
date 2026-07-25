"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root])
        res = []
        while q:
            l = len(q)
            level = []
            for _ in range(l):
                node = q.popleft()
                if not node:
                    continue
                level.append(node)
                q.append(node.left)
                q.append(node.right)

            res.append(level)

        # [[l1],[l2,l21,l23],[l3,l31,l32,l34]]

        for level in res:
            l = len(level)
            for i in range(l-1):
                level[i].next = level[i+1]

        return root