# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return None
        while head != None and head.val==val:
            head=head.next
        if head==None:
            return None
        current=head
        prev=current
        
        while current:
            if current.val==val:
                prev.next=current.next
            else:
                prev=current
            current=current.next
        return head