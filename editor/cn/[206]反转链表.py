
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # 反转链表需要维护三个结点：prev、curr、next_node

        prev = None
        curr = head

        while curr:
            # 把下一个结点拿出来
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
        
# leetcode submit region end(Prohibit modification and deletion)
