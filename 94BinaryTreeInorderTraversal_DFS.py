from collections import deque
from typing import Optional, List

# 1. Define the TreeNode class so Python knows what it is
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2. Your actual solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r = []
        q = deque()
        node = root  
        
        while node or q: 
            if node:
                q.append(node)
                node = node.left
            else:
                node = q.pop()
                r.append(node.val)  
                node = node.right
                
        return r

# --- Example of how to test it locally ---
if __name__ == "__main__":
    # Building the tree: [1, null, 2, 3]
    #      1
    #       \
    #        2
    #       /
    #      3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    # Running your solution
    sol = Solution()
    print(sol.inorderTraversal(root))  # Output should be: [1, 3, 2]
