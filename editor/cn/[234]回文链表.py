
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 快慢指针+ 反转链表
        if not head or not head.next:
            return head

        # 找到链表的中间结点：使用快慢指针
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # 此时slow的当前结点就是链表的中间结点

        # 反转后半部分链表：反转两边是两两调换，修改链表方向
        # 实现反转链表需要维护三个指针，prev、curr、next_node
        # 反转后链表的前一个结点和当前结点
        prev = None    # prev初始化为none，作为反转链表的尾部
        curr = slow.next
        while curr:
            next_node = curr.next   # 保存当前结点的下一个结点
            curr.next = prev    # 当前结点的next指针指向前一个结点，实现反转
            prev = curr # 更新prev指针当前结点
            curr = next_node # 更新curr指针为下一个结点

        # 比较前部分和后部分的反转链表
        first_half = head
        second_half = prev  # 经过反转链表好，prev就是反转链表的头结点
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True

# leetcode submit region end(Prohibit modification and deletion)
