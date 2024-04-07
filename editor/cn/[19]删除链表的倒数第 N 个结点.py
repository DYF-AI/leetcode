# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        """
        分析:
            1.链表+双指针（快指针、慢指针）；
            2.初始时，将两个指针都指向虚拟结点dummy；
            3.快指针先向前移动n步；
            4.然后，同时移动快指针和慢指针，直至快指针到达链表的末尾，
              此时慢指针指向的结点就是需要删除的结点的前一个结点；
            5.删除倒数第n个结点：将慢指针指向的结点的下一个结点指向下下个结点，
              即跳过倒数的第n个结点；
            6.返回虚拟头结点的下一个结点作为新的头结点，如果原始链表为空，返回None；

            # 快指针的作用主要是定位
            只遍历一次链表，时间复杂度O(N)
        """

        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # 将快指针向前移动n步
        for _ in range(n):
            fast = fast.next

        # 同时移动快指针和慢指针，直至快指针到达链表的末尾
        while fast.next:
            fast = fast.next
            slow = slow.next

        # 删除倒数第n个结点
        slow.next = slow.next.next

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
