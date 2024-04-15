
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # 方法1：二叉树+回溯法

        if not root:
            return root
        result = []
        def backtrack(node, curr_path):
            if not node:
                return
            curr_path.append(node.val)
            # 需要检查是否到叶子结点,叶子结点是没有左右子结点
            if not node.left and not node.right and sum(curr_path) == targetSum:
                result.append(curr_path[:])

            backtrack(node.left, curr_path[:])
            backtrack(node.right, curr_path[:])

            curr_path.pop()

        backtrack(root, [])
        return result


        
# leetcode submit region end(Prohibit modification and deletion)
