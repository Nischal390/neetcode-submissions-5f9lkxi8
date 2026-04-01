# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        lot = []
        q.append(root)

        while q:
            Qlen = len(q)
            items = []
            for i in range(Qlen):
                node = q.popleft()
                if node:
                    items.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if items:
                lot.append(items.pop())

        return lot
        
