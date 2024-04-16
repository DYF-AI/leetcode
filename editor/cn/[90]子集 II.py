
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 组合：一维数组+回溯法
        result = []
        # 解集不能出现重复元素
        nums.sort()
        def backtrack(start, curr_subset):
            result.append(curr_subset[:])
            if len(curr_subset) == len(nums):
                return
            for i in range(start, len(nums)):
                # 解集不能出现重复元素
                if i>start and nums[i] == nums[i-1]:
                    continue
                curr_subset.append(nums[i])
                # 因为解集不能出现重复子集
                backtrack(i+1, curr_subset)
                curr_subset.pop()

        backtrack(0, [])
        return result



# leetcode submit region end(Prohibit modification and deletion)
