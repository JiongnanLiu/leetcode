"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        first_half_end = self.endOfFirstHalf(head)
        second_half_start = self.reverseLinkedList(first_half_end.next)
                
        
        temp1 = head
        temp2 = second_half_start
        
        while temp2:
            if temp2.val != temp1.val:
                return False
            temp2=temp2.next
            temp1=temp1.next
            
        first_half_end.next = self.reverseLinkedList(second_half_start)
        return True
        
    def endOfFirstHalf(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
            
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        prev = None
        current = head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        return prev