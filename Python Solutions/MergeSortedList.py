# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1=[]
        li=l1
        list2=[]
        li2=l2
        while li is not None:
            list1.append(li.val)
            li=li.next
        
        while li2 is not None:
            list2.append(li2.val)
            li2=li2.next
        
        list3=list1+list2
        list3.sort()
        return list3