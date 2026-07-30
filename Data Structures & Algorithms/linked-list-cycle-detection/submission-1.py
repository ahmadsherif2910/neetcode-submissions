# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        dummy = ListNode()
        dummy = head
        while dummy:
            if id(dummy) in sett:
                return True
            sett.add(id(dummy))
            dummy=dummy.next
        return False