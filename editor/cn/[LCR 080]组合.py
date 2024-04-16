
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 组合：回溯法

        result = []

        def backtrack(start, curr_combination):
            if len(curr_combination) == k:
                result.append(curr_combination[:])
                return
            for j in range(start, n+1):
                # 做选择
                curr_combination.append(j)
                # 递归
                backtrack(j+1, curr_combination)
                # 回溯
                curr_combination.pop()

        backtrack(1, [])
        return result



# leetcode submit region end(Prohibit modification and deletion)
