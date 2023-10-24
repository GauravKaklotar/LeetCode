# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        def levelOrder(root):
            if root is None: return []
            path = []
            q = deque()
            q.append(root)
            while q:
                n = len(q)
                temp = []
                for _ in range(n):
                    node = q.popleft()
                    temp.append(node.val)
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                path.append(temp)
            return path
        
        path = levelOrder(root)
        return [max(l) for l in path]