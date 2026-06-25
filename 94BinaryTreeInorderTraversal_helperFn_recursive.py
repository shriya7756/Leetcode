from collections import deque
from typing import Optional, List

# 1. Define the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Your Solution class
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        
        # I kept your exact logic. Note: 'root' here shadows the outer 'root', 
        # which is perfectly valid in Python!
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            r.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return r

# 3. The Test Block (This allows the script to run locally)
if __name__ == "__main__":
    # Let's build the standard LeetCode test case: [1, null, 2, 3]
    # Visually, the tree looks like this:
    #      1
    #       \
    #        2
    #       /
    #      3
    
    # Building the nodes
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    
    # Connecting the nodes
    node1.right = node2
    node2.left = node3
    
    # Initialize your Solution class
    sol = Solution()
    
    # Run the function and print the result
    result = sol.inorderTraversal(node1)
    print(f"Inorder Traversal Output: {result}")  # Expected Output: [1, 3, 2]

