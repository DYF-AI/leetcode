
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        combinations = []

        def backtrack(curr_candidate, start):
            if len(curr_candidate) == k:
                return combinations.append(curr_candidate[:])
            for i in range(start, n+1):
                curr_candidate.append(i)
                backtrack(curr_candidate, i+1)
                curr_candidate.pop()

        backtrack([], 1)
        return combinations

# leetcode submit region end(Prohibit modification and deletion)
