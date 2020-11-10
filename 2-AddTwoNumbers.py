# Time Complexity O(max(m,n))
# Spaxe Complexity O(nmax(m+n), or O(nmax(m+n)+1 in the worst case
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        root = n = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            curr = 0
            if l1:
                curr += l1.val
                l1 = l1.next
            
            if l2:
                curr += l2.val
                l2 = l2.next
                
            if carry != 0:
                curr += carry
                carry = 0
                
            n.next = ListNode(curr%10)
            carry = curr//10
            n = n.next
        return root.next
    