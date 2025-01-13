# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next==None or k==0:
            return head
        temph=head
        n=1
        while temph.next:
            n+=1
            temph=temph.next
        k=k%n
        if k==0:
            return head
        last=head
        pre=head
        for i in range(k):
            last=last.next
        while last.next:
            pre=pre.next
            last=last.next
        pt=pre.next
        last.next=head
        pre.next=None
        return pt



