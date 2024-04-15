
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        combinations = []

        digit_alpha_mapping = {

            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(start, curr_candidate):
            # start是从第start个数字开始回溯
            if start == len(digits):
                combinations.append(curr_candidate)
                return
            candidate_alpha = digit_alpha_mapping[digits[start]]

            for letter in candidate_alpha:
                # 做选择
                curr_candidate += letter
                # 递归
                backtrack(start + 1, curr_candidate)
                # 回溯
                curr_candidate = curr_candidate[:-1]

        backtrack(0, "")
        return combinations

        # if not digits:
        #     return []
        #
        #     # 构建数字到字母的映射关系
        # digit_map = {
        #     '2': 'abc',
        #     '3': 'def',
        #     '4': 'ghi',
        #     '5': 'jkl',
        #     '6': 'mno',
        #     '7': 'pqrs',
        #     '8': 'tuv',
        #     '9': 'wxyz'
        # }
        #
        # combinations = []
        #
        # def backtrack(start, curr_combination):
        #     if start == len(digits):
        #         combinations.append(curr_combination)
        #         return
        #     for letter in digit_map[digits[start]]:
        #         backtrack(start + 1, curr_combination + letter)
        #
        # backtrack(0, '')
        # return combinations






# leetcode submit region end(Prohibit modification and deletion)
