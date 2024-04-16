
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 组合：一维数组+回溯

        result = []
        def backtrack(start, curr_set):
            # 添加当前路径到解集
            result.append(curr_set[:])
            for i in range(start, len(nums)):
                curr_set.append(nums[i])
                backtrack(i+1, curr_set)
                curr_set.pop()
        backtrack(0, [])
        return result



# leetcode submit region end(Prohibit modification and deletion)
