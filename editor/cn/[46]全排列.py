# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutations = []

        def backtrack(curr_permutation):
            # 如果当前序列的长度等于数组的长度，说明是一个完整的排列
            if len(curr_permutation) == len(nums):
                permutations.append(curr_permutation[:])
                return
            # 对于当前位置，尝试将数组中每个没使用的原始进入到排列中
            for num in nums:
                if num not in curr_permutation:
                    # 做选择
                    curr_permutation.append(num)
                    # 递归
                    backtrack(curr_permutation)
                    # 回溯
                    curr_permutation.pop()

        backtrack([])
        return permutations


# leetcode submit region end(Prohibit modification and deletion)

"""
回溯法
    - 回溯法通常用于解决组合、排列、搜索等问题。
    - 回溯法的核心思想是通过递归实现，在每一步都尝试一种可能性

回溯法的步骤：
1、选择：做出一个选择，通常是在当前状态下可以做的选中的一个
2、递归：基于所做的选择，进入下一个状态，并继续进行选择
3、回溯：如果在当前状态下的所有选择都已经尝试过，或者到达了结束条件，
    但没有找到解答，则回溯到上一个状态，撤销上一步选择，并尝试其它选择
    
一句话：做选择、递归、回溯
    




"""
