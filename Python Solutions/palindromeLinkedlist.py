# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans=list()
        while head:
            ans.append(head.val)
            head=head.next
        
        reverse=ans[::-1]
        if reverse==ans:
            return True
        return False
        