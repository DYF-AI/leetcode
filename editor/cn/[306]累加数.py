
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # 如何确定第1、2个数？
        # 使用暴力法+回溯法，穷举

        # 使用前两层for循环，确定数字num1, num2
        # 调用回溯法，里面还有个for循环，判断num1+num2=num3

        def backtrack(start, num1, num2):
            if start == len(num):
                return True
            for end in range(start+1, len(num)+1):
                num3_str = num[start:end]
                if (len(num3_str)>1 and num3_str[0]=="0") or \
                    len(num3_str) > len(num)//2+1:
                    # 不以0为开头且长度不能超过剩余长度的一般
                    # 其实就是在做剪枝
                    break
                num3 = int(num3_str)
                if num3 == num1 + num2:
                    if backtrack(end, num2, num3):
                        return True
                elif num3 > num1+num2:
                    break

            return False



        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                num1_str = num[:i]
                num2_str = num[i:j]

                if (len(num1_str) > 1 and num1_str[0] == "0") or \
                        (len(num2_str) > 1 and num2_str[0] == "0"):
                    # 数字不能以0为开头
                    continue
                num1, num2 = int(num1_str), int(num2_str)
                if backtrack(j, num1, num2):
                    return True

        return False



# leetcode submit region end(Prohibit modification and deletion)
