"""
SOLUTION 1 - ELEMENTARY MATH
Time Complexity: O(n)
Space Complexity: O(n)
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
 
 
 """
 SOLUTION 2 - NAIVE PYTHON BUILT-IN FUNCTIONS APPROACH
 Time Complexity: O(n)
 Space Complexity: O(n)
 """

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1_reversed = ""
        num2_reversed = ""
        while l1 is not None:
            num1_reversed += str(l1.val)
            l1 = l1.next
        while l2 is not None:
            num2_reversed += str(l2.val)
            l2 = l2.next
        num1 = num1_reversed[::-1]
        num2 = num2_reversed[::-1]
        result = int(num1) + int(num2)
        result_reversed = str(result)[::-1]
        head = ListNode(result_reversed[0])
        iterator = head
        n = len(result_reversed)
        for i in range(1, n):
            iterator.next = ListNode(result_reversed[i])
            iterator = iterator.next
        iterator.next = None
        return head
