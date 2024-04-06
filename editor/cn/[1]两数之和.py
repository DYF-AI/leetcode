# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 解法很多：
        # # 解法1: 双指针, 需要先排序.不是最优解
        # # 犹豫返回的是index，排序时需要记录一下index, 如果返回的是数值，则不需要index
        # left, right = 0, len(nums) - 1
        # num_with_index = [(num,index) for index, num in enumerate(nums)]
        # num_with_index.sort()
        #
        # while left < right:
        #     total = num_with_index[left][0] + num_with_index[right][0]
        #     if total == target:
        #         return [num_with_index[left][1], num_with_index[right][1]]
        #     elif total > target:
        #         right -= 1
        #     else:
        #         left += 1

        # 解法2： hash表
        # 用于存储数字与其索引,是存储数字和索引
        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            # 每次都判断一下是否已经存在需要找的差值
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i
        return None



# leetcode submit region end(Prohibit modification and deletion)
