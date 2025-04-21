# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2
        added = ListNode(0)
        head = added
        carry = 0
        while curr1 or curr2:
            num1, num2 = 0, 0
            if curr1:
                num1 = curr1.val
                curr1 = curr1.next
            if curr2:
                num2 = curr2.val
                curr2 = curr2.next
            sm = str(num1+num2+carry)
            added.next = ListNode(int(sm[-1]))
            added = added.next
            carry = int(sm[0]) if len(sm)>1 else 0
        added.next = ListNode(int(carry)) if carry else None
        return head.next
        #return int(added+(str(carry) if carry else ""))