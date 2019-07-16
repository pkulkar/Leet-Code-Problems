# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        marker1 =head
        marker2 =head
    
        while marker2 !=None and marker2.next!=None:
            marker1=marker1.next
            marker2=marker2.next.next
            if marker2==marker1:
                return True
        return False
    
        