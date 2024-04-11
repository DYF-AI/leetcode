
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 排列和组合，使用回溯法
        # 构建回溯递归函数

        """
        #没有考虑候选数字的去重问题：在递归过程中，没有考虑到同一个数字可以重复使用的情况，因此可能会导致结果中包含重复的组合。
        #没有考虑剪枝优化：在搜索过程中，没有进行剪枝优化，可能会导致不必要的搜索。
        #缺少对候选数字排序：为了避免重复搜索相同的组合，应该对候选数字进行排序。
        #未正确处理递归函数参数：在递归函数
        #backtrack
        #中，应该传递当前搜索的起始位置，而不是直接传递
        #curr_candidate。
        result = []
        def backtrack(curr_candidate):
            if sum(curr_candidate) == target:
                result.append(curr_candidate[:])
                return
            for candidate in candidates:
                curr_candidate.append(candidate)
                backtrack(curr_candidate)
                curr_candidate.pop()
        backtrack([])
        return result
        """

        result = []

        def backtrack(start, curr_candidate):
            total = sum(curr_candidate)
            if total == target:
                result.append(curr_candidate[:])
                return
            # 如果大于直接返回
            if total > target:
                return
            for i in range(start,len(candidates)):
                # 做选择
                curr_candidate.append(candidates[i])
                # 递归
                backtrack(i,curr_candidate)
                # 回溯
                curr_candidate.pop()

        backtrack(0, [])
        return result



# leetcode submit region end(Prohibit modification and deletion)
