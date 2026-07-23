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
    def level_order(self, node):
        if not node:
            return node
        res = []
        queue = deque()
        queue.append(node)
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):   
                curr = queue.popleft()
                level.append(curr)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            res.append(level)

        return res
            
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        res = self.level_order(root)

        for list_ in res:
            for i in range(len(list_)-1):
                list_[i].next = list_[i+1]

        return root


        
            
