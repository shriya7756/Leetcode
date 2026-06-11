# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        q=deque([root])
        while q:
            lev_len=len(q)
            for i in range(lev_len):
                n=q.popleft()
                if i==lev_len-1:
                    res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return res
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
    sol = Solution()
    result = sol.rightSideView(root)
    
    print(f"Right side view: {result}") 
    # Expected output: Right side view: [1, 3, 4]
