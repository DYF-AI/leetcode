
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 分析: [1,0,-1,-2,2], 必须是四元组
        # 数组都可以考虑排序 排序: [-2,-1,0,1,2]
        # 双指针, left, right
        # 双执政只能固定两个数值， 需要再套两层循环
        # 也可在三数之和的基础上，再增加一层循环

        # # 解法1： 双指针
        # nums.sort()
        # n = len(nums)
        # res = []
        # # 第一层控制第一个元素num[i]
        # for i in range(n - 3):
        #     # 避免重复
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     # 第二层控制第二个元素num[j]
        #     for j in range(i + 1, n - 2):
        #         # 避免重复
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #         # 双指针找到另外两个符合要求的元素
        #         left, right = j + 1, n - 1
        #         while left < right:
        #             total = nums[i] + nums[j] + nums[left] + nums[right]
        #             if total == target:
        #                 res.append([nums[i], nums[j], nums[left], nums[right]])
        #                 # 避免重复
        #                 while left < right and nums[left] == nums[left + 1]:
        #                     left += 1
        #                 while left < right and nums[right] == nums[right - 1]:
        #                     right -= 1
        #                 left += 1
        #                 right -= 1
        #             elif total < target:
        #                 left += 1
        #             else:
        #                 right -= 1
        # return res

        # 解法2： 组合, 该方法可以求解任何的Nsum问题
        # 通过递归的方式将N数之和拆解为两数之和，再利用双指针技术解决两数之和
        def findNSum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    total = nums[left] + nums[right]
                    if total == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]], results)

        results = []
        findNSum(sorted(nums), target, 4, [], results)
        return results


# leetcode submit region end(Prohibit modification and deletion)
