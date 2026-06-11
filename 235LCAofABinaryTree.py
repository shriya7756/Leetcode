class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start at the root
        cur = root
        
        # The while loop will naturally handle the case where root is None
        while cur:
            if p.val < cur.val and q.val < cur.val:
                # Both targets are smaller, move left
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                # Both targets are larger, move right
                cur = cur.right
            else:
                # We found the point where they split or where one is the ancestor of the other
                return cur
