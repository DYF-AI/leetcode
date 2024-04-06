# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 双指针
        nums.sort()
        n = len(nums)
        result = []

        # 因为需要至少三个数字, i的范围是n-2
        for i in range(n - 2):
            # 跳过重复的数字,题目要求不包含重复的三元组
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # 跳过重复数字，题目要求不包含重复的三元组
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # 跳过重复数字，题目要求不包含重复的三元组
                    while left < right and [right] == nums[right + 1]:
                        right -= 1
                # 比目标值小, 左侧滑动
                elif total < 0:
                    left += 1
                # 比目标值小, 右侧滑动
                else:
                    right -= 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
