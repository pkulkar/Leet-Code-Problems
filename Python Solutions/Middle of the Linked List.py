# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=head
        count=0
        while node:
            count+=1
            node=node.next
        node=head
        recur=node
        i=0
        while i<count:
            node1=head.next
            head=node1
            if i==round(count/2)-1:
                node=head
                recur=node
            if i>round(count/2)-1:
                recur.next=node1
                recur=recur.next
            i+=1
        return node