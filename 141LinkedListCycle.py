from typing import Optional

# 1. Define the ListNode class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2. Your Solution class
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        s = head
        f = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f:
                return True
        return False

# 3. Driver code to test the solution locally
if __name__ == "__main__":
    solution = Solution()

    # --- Test Case 1: Linked List WITH a cycle ---
    # Create nodes: [3, 2, 0, -4]
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    # Link nodes: 3 -> 2 -> 0 -> -4
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # Create the cycle: point tail (-4) back to node 2
    node4.next = node2 

    print("Test Case 1 (Expect True):", solution.hasCycle(node1))

    # --- Test Case 2: Linked List WITHOUT a cycle ---
    # Create nodes: [1, 2]
    nodeA = ListNode(1)
    nodeB = ListNode(2)

    # Link nodes: 1 -> 2 -> None
    nodeA.next = nodeB

    print("Test Case 2 (Expect False):", solution.hasCycle(nodeA))
