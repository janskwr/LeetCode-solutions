"""
SOLUTION 1
Time Complexity: O(n)
"""

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_sum = ListNode()
        pointer_l1 = l1
        pointer_l2 = l2
        pointer_lsum = l_sum
        carry = 0
        while (pointer_l1 != None or pointer_l2 != None):
            if pointer_l1 == None:
                x = 0
            else:
                x = pointer_l1.val
            if pointer_l2 == None:
                y = 0
            else:
                y = pointer_l2.val
            suma = x + y + carry
            carry = suma // 10
            pointer_lsum.next = ListNode(suma % 10)
            pointer_lsum = pointer_lsum.next
            if pointer_l1 != None:
                pointer_l1 = pointer_l1.next
            if pointer_l2 != None:
                pointer_l2 = pointer_l2.next
        if carry > 0:
            pointer_lsum.next = ListNode(carry)
        return l_sum.next
    
