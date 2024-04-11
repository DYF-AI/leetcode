
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        if left == right:
            return head

        # dummy指向原始链表的头结点
        dummy = ListNode(0)
        dummy.next = head
        pre
        _left = dummy

        # 根据提供的 heft、right，将链表切成3块
        # 使用快慢指针

        #part1 = head
        for i in range(left-1):
            pre_left = pre_left.next

        prev = None
        curr = pre_left.next

        for _ in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        pre_left.next.next = curr
        pre_left.next = prev

        # 一开始dummy.next是head，所有返回dummy.next
        return dummy.next





        
# leetcode submit region end(Prohibit modification and deletion)
