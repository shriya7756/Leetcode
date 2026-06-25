from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = 0
        q = deque([root])
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            d = d + 1
        return d

# --- Driver Code for Testing ---
if __name__ == "__main__":
    # Create an instance of your solution
    sol = Solution()

    # Example 1: root = [3,9,20,null,null,15,7]
    # Building the tree manually
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    depth1 = sol.maxDepth(root1)
    print(f"Example 1 Output: {depth1}")  # Expected output: 3

