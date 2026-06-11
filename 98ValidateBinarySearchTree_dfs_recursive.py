from typing import Optional

# 1. Define the structure of a tree node (LeetCode hides this part)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Your solution class
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(n, min_val, max_val):
            # Base case: empty node is valid
            if not n:
                return True
            
            # Check if the current node's value violates the boundaries
            if not (max_val > n.val > min_val):
                return False
            
            # Recursively check left and right subtrees
            return valid(n.left, min_val, n.val) and valid(n.right, n.val, max_val)
        
        # Start the recursion with absolute boundaries
        return valid(root, float("-inf"), float("inf"))

# 3. Test cases to run the code
if __name__ == "__main__":
    # Initialize the solution
    sol = Solution()

    print("--- Testing Valid BST ---")
    # Building Tree 1: [2, 1, 3]
    #       2
    #      / \
    #     1   3
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)
    
    result1 = sol.isValidBST(root1)
    print(f"Tree 1 is valid: {result1} (Expected: True)")


    print("\n--- Testing Invalid BST ---")
    # Building Tree 2: [5, 1, 4, null, null, 3, 6]
    #       5
    #      / \
    #     1   4
    #        / \
    #       3   6
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)
    
    result2 = sol.isValidBST(root2)
    print(f"Tree 2 is valid: {result2} (Expected: False)")
