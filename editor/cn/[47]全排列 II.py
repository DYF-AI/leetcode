
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # permutations = []
        # permutations_str = []
        #
        # def backtrack(curr_permutation):
        #     if len(curr_permutation) == len(nums):
        #         curr_permutation_str = "".join([str(digit) for digit in curr_permutation])
        #         if curr_permutation_str not in permutations_str:
        #             permutations.append(curr_permutation[:])
        #             permutations_str.append(curr_permutation_str)
        #         return
        #
        #     for num in nums:
        #         curr_permutation.append(num)
        #         backtrack(curr_permutation)
        #         curr_permutation.pop()
        # backtrack([])
        # return permutations


        def backtrack(curr_permutation):
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:])
                return
            for i in range(len(nums)):
                # 如果当前元素已经在排列中，跳过
                # 如果used=True跳过，后面数个前面一个数相当且used[i-1]为False（没使用）
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                used[i] = True
                curr_permutation.append(nums[i])
                backtrack(curr_permutation)
                used[i] = False
                curr_permutation.pop()

        permutations = []
        used = [False] * len(nums)
        nums.sort()  # 排序数组
        backtrack([])
        return permutations



# leetcode submit region end(Prohibit modification and deletion)
