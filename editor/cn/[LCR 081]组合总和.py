
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 组合：一维数组+回溯法

        result = []
        #candidates.sort()
        def backtrack(start, curr_candidate):
            if sum(curr_candidate) == target:
                result.append(curr_candidate[:])
                return
            if sum(curr_candidate) > target:
                return

            for i in range(start, len(candidates)):
                curr_candidate.append(candidates[i])
                # 因为candidates中的数字可以无限重复使用，所有这里为i
                backtrack(i, curr_candidate)
                curr_candidate.pop()

        backtrack(0, [])
        return result

# leetcode submit region end(Prohibit modification and deletion)
