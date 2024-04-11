
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = "".join([str(digit) for digit in digits])
        digits = int(digits_str) + 1
        digits = [int(ch) for ch in str(digits)]
        return digits
# leetcode submit region end(Prohibit modification and deletion)
