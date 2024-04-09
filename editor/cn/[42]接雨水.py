
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 分析：还是先用双指针吧
        if not height:
            return 0
        # 初始化两个指针，分别指向数组的开头和结尾
        left, right = 0, len(height) - 1
        # 初始化两个变量，分别表示left左边的最高柱子和右边right的最高柱子
        max_left, max_right = 0, 0
        # 记录接到雨水的数量
        water = 0

        # 双指针
        while left <= right:
            # 重点看指针如何滑动
            if height[left] < height[right]:
                # 左侧最高
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    # 只有当height[left] <= max_left, 才能计算雨水，毕竟要有坑要能装
                    water += (max_left - height[left])
                # 左侧指针移动
                left += 1
            else:
                # 保留右侧最高
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    # 只有当height[right] <= max_right, 才能计算雨水，毕竟要有坑要能装
                    water += (max_right - height[right])
                # 右侧指针
                right -= 1

        return water
# leetcode submit region end(Prohibit modification and deletion)


"""
代码解释流程

1. 初始化左指针 left = 0，右指针 right = 11（数组的第一个和最后一个索引），
   以及两个最大高度变量 max_left = 0 和 max_right = 0。
2. 开始循环，由于 left <= right，因此进入循环：
    在第一次迭代中，height[left] = 0，height[right] = 1。
    由于 height[left] < height[right]，所以进入第一个分支。
        由于 height[left] > max_left（0 > 0），
        更新 max_left = height[left]。
        left 指针向右移动一位，left = 1。
    在第二次迭代中，height[left] = 1，height[right] = 1。
    由于 height[left] == height[right]，所以进入第二个分支。
        由于 height[right] > max_right（1 > 0），
        更新 max_right = height[right]。
        right 指针向左移动一位，right = 10。
    在第三次迭代中，height[left] = 1，height[right] = 2。
        由于 height[left] < height[right]，所以进入第一个分支。
        由于 height[left] < max_left（1 < 1），
        计算雨水量 water += max_left - height[left] = 1 - 1 = 0。
        left 指针向右移动一位，left = 2。
    迭代继续，直到 left > right 时退出循环。
3.最终返回雨水量 water = 6。

"""