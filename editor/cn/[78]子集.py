
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 互不相同，说明不用考虑重复子集了

        result = []

        def backtrack(start, curr_subset):
            # [:] python2的写法，leetcode底层框架应该是使用python2
            result.append(curr_subset[:])

            for i in range(start, len(nums)):
                curr_subset.append(nums[i])
                backtrack(i+1, curr_subset)
                curr_subset.pop()

        backtrack(0,[])
        return result


# leetcode submit region end(Prohibit modification and deletion)
