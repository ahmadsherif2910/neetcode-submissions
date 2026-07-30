# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        dummy = head
        while dummy:
            if dummy in sett:
                return True
            sett.add(dummy)
            dummy=dummy.next
        return False