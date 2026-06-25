from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res, q = [], deque([root])
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
                    
            res.append(level)
        
        return res

# --- Example Usage for IDLE ---
if __name__ == "__main__":
    sol = Solution()

    # Constructing a sample binary tree:
    #      3
    #    /   \
    #   9    20
    #       /  \
    #      15   7
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = sol.levelOrder(root)
    print(f"Level order traversal: {result}") 
    # Expected output: [[3], [9, 20], [15, 7]]

