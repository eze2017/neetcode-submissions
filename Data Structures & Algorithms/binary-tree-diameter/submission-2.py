# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        For any specific node in the tree, what is the longest possible path that must pass through it? 
        It is the sum of the maximum depths (heights) of its left and right subtrees.
        Key Idea: If a node's left subtree has a height of $L$ and its right subtree has a height of $R$,
        the longest path going through that node is $L + R$.
        """

        max_diameter = 0  #
        def get_height(node):
            # base case if node is empty:
            if not node:
                return  -1
                # Using -1 helps treat a leaf node as height 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            nonlocal max_diameter
            # Calculate "local" diameter at this specific node
            # Diameter is the path from the deepest left leaf to the deepest right leaf
            curr_diameter = (left_height+1)+(right_height+1)
            # Update the global maximum diameter found so far
            max_diameter = max(max_diameter,curr_diameter)
            return 1+max(left_height, right_height)
        get_height(root)
        return max_diameter

