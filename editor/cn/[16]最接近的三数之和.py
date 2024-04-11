import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 双指针（先固定一个数，再使用双指针）
        nums.sort()
        three_sum_closest = float('inf')
        for i in range(len(nums)-2):
            num_i = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                # 重点看滑动方向
                three_sum = num_i + nums[left] + nums[right]
                if abs(target-three_sum) < abs(target-three_sum_closest):
                    three_sum_closest = three_sum
                if three_sum < target:
                    left += 1
                elif three_sum > target:
                    right -= 1
                else:
                    return target
        return three_sum_closest



# leetcode submit region end(Prohibit modification and deletion)
