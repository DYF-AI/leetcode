
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 重点解集不能重复，需要排序
        candidates.sort()

        result = []
        def backtrack(start, curr_candidate):
            total = sum(curr_candidate)
            if total == target:
                result.append(curr_candidate[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # 避免集合重复，之前已经排序
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr_candidate.append(candidates[i])
                # 因为candidates的每个数字在每个集合中只能只有一次，所以是i+1
                backtrack(i+1, curr_candidate)
                curr_candidate.pop()

        backtrack(0, [])
        return result

# leetcode submit region end(Prohibit modification and deletion)
