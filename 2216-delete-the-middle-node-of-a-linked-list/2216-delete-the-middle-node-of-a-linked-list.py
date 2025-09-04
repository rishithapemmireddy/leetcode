# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return None

        turtle = head
        hare = head
        prev = None

        # Find middle node
        while hare and hare.next:
            prev = turtle
            turtle = turtle.next
            hare = hare.next.next

        # Delete the middle node
        prev.next = turtle.next

        return head