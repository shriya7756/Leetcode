from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        
        q = deque([root.left, root.right])
        
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            
            if not t1 and not t2: 
                continue
            if not t1 or not t2 or t1.val != t2.val: 
                return False
            
            q.extend([t1.left, t2.right, t1.right, t2.left])
            
        return True

# --- Example Usage for IDLE ---
if __name__ == "__main__":
    sol = Solution()

    # --- Test Case 1: Symmetric Tree ---
    #         1
    #       /   \
    #      2     2
    #     / \   / \
    #    3   4 4   3
    
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))

    print(f"Is tree 1 symmetric? {sol.isSymmetric(root1)}") 
    # Expected output: True

    # --- Test Case 2: Asymmetric Tree ---
    #         1
    #       /   \
    #      2     2
    #       \     \
    #        3     3
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))

    print(f"Is tree 2 symmetric? {sol.isSymmetric(root2)}") 
    # Expected output: False
