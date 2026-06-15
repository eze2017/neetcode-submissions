# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if not root:
             return
        queue.append(root)
        while len(queue) > 0:
            current_node = queue.pop()
            current_node.left ,current_node.right = current_node.right,current_node.left
           
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return root
