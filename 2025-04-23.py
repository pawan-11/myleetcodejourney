

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        newlst = None
        newcurr = None
        while curr:
            print("curr:",curr.val)
            nxt = curr.next
            dups = 0
            while nxt and nxt.val == curr.val:
                dups += 1
                nxt = nxt.next
            print(curr.val, "dups:",dups)
            print(newlst)
            if dups == 0:
                if newcurr:
                    newcurr.next = curr
                else:
                    newlst = curr
                    newcurr = newlst
                curr = curr.next
            else:
                curr = nxt
        return newlst
                

