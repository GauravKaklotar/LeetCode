# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        stack = []
        if root is None: return
        stack.append(root)
        while len(stack):
            temp = []
            for i in range(len(stack)):
                node = stack[0]
                stack = stack[1:]
                temp.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            ans.append(temp)
        return ans