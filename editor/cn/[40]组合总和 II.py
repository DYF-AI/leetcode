
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 回溯法
        combinations = []
        # 不使用used，而是通过传参数start来控制没一层递归其实的位置
        def backtrack(curr_candidate, start):
            total = sum(curr_candidate)
            if total == target:
                combinations.append(curr_candidate[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                # 因为前面使用了排序，可以使用candidates[i] == candidates[i - 1]避免重复组合
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # 避免重复组合
                curr_candidate.append(candidates[i])
                backtrack(curr_candidate, i + 1)
                curr_candidate.pop()

        candidates.sort()  # 排序以便剪枝
        backtrack([], 0)
        return combinations





# leetcode submit region end(Prohibit modification and deletion)
