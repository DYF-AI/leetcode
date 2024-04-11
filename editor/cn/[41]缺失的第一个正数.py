# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        n = 1
        while n in num_set:
            n += 1
        return n

# leetcode submit region end(Prohibit modification and deletion)
