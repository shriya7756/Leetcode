from typing import Optional

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
        
        def isMirror(t1, t2):
            if not t1 and not t2: 
                return True
            if not t1 or not t2: 
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
            
        return isMirror(root.left, root.right)

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

    result1 = sol.isSymmetric(root1)
    print(f"Is tree 1 symmetric? {result1}") 
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

    result2 = sol.isSymmetric(root2)
    print(f"Is tree 2 symmetric? {result2}") 
    # Expected output: False
