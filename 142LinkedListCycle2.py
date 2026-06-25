from typing import Optional

# 1. Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 2. Your Solution Class
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No cycle
        
        # Step 2: Find the cycle entry point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow

# 3. Driver Code to test the solution
if __name__ == "__main__":
    # Let's recreate Example 1 from LeetCode: head = [3,2,0,-4], pos = 1
    
    # Create the individual nodes
    node0 = ListNode(3)
    node1 = ListNode(2)
    node2 = ListNode(0)
    node3 = ListNode(-4)
    
    # Link the nodes to form the list: 3 -> 2 -> 0 -> -4
    node0.next = node1
    node1.next = node2
    node2.next = node3
    
    # Create the cycle: tail (-4) connects to node index 1 (value: 2)
    node3.next = node1 
    
    # Instantiate the solution and run it
    sol = Solution()
    cycle_start_node = sol.detectCycle(node0)
    
    # Print the output
    if cycle_start_node:
        print(f"Cycle detected! The cycle begins at node with value: {cycle_start_node.val}")
    else:
        print("No cycle detected.")
