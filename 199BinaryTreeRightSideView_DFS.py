from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node, depth):
            if not node:
                return
            
            # If the current depth is equal to the length of our result list,
            # it means we are visiting this level for the very first time.
            if depth == len(res):
                res.append(node.val)
            
            # Traverse the right side first, then the left side.
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
            
        dfs(root, 0)
        return res

# --- Example Usage for IDLE ---
if __name__ == "__main__":
    # Constructing a sample binary tree:
    #      1
    #    /   \
    #   2     3
    #    \     \
    #     5     4
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    # Instantiate the Solution class and run the method
    sol = Solution()
    result = sol.rightSideView(root)
    
    print(f"Right side view (DFS): {result}") 
    # Expected output: Right side view (DFS): [1, 3, 4]

