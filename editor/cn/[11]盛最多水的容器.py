# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def calArea(self, h1, h2, x1, x2):
        min_h = min(h1, h2)
        return min_h * (x2 - x1)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 双指针
        max_area, n = 0, len(height)
        left, right = 0, n - 1

        while left < right:
            area = self.calArea(height[left], height[right], left, right)
            if area >= max_area:
                max_area = area
            # 划重点:向高度较高的一侧移动
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# leetcode submit region end(Prohibit modification and deletion)
