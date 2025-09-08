# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if not head or not head.next:
            return True
        middle = self.findmiddle(head)
        head2=self.reverse(middle)
        head1=head

        while head2!=None:
            if head1.val !=  head2.val:
                return False
            else:
                head1=head1.next
                head2=head2.next
        return True

    def findmiddle(self,head):
        turtle = head
        fast=head
        while fast != None and fast.next!= None:
            fast=fast.next.next
            turtle=turtle.next
        return turtle

    def reverse(self, head):
        prev=None
        curr=head
        while curr is not None:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
        return prev
        