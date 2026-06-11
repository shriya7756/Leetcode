# 1. Define the ListNode structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. The solution class
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dum = ListNode(0)
        carry = 0
        cur = dum
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            t = v1 + v2 + carry
            carry = t // 10
            cur.next = ListNode(t % 10)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dum.next

# 3. Helper code to convert lists to Linked Lists for testing
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# 4. Helper code to print the Linked List
def print_linked_list(node):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    print(" -> ".join(vals))

# --- Testing the code ---
if __name__ == "__main__":
    # Example: l1 = [2,4,3] (which is 342), l2 = [5,6,4] (which is 465)
    # Result should be [7,0,8] (which is 807)
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    
    print("Result:")
    print_linked_list(result)
