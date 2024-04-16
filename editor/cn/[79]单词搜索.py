# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # def exist(self, board, word):
    #     """
    #     :type board: List[List[str]]
    #     :type word: str
    #     :rtype: bool
    #     """
    #     # 分析：算是一个路径判断, 类似N皇后
    #     # 1、不能被重复使用，需要使用visited矩阵记录cell是否已经被使用了
    #     #
    #
    #     # 方法1：矩阵+回溯法  两层for循环+上下左右回溯 暴力求解
    #     if not board:
    #         return False
    #     rows, cols = len(board), len(board[0])
    #     visited = [[False] * cols for _ in range(rows)]
    #
    #     def backtrack(row, col, index):
    #         # 如果索引越界或者当前字符不匹配，返回False
    #         if row < 0 or row >= rows or col < 0 or col >= cols \
    #                 or board[row][col] != word[index] \
    #                 or visited[row][col]:
    #             return False
    #         # 如果找到整个单词，返回True
    #         if index == len(word) - 1:
    #             return True
    #
    #         # 标记当前位置已访问
    #         visited[row][col] = True
    #
    #         # 递归搜索上、下、左、右四个方向
    #         found = backtrack(row - 1, col, index + 1) or \
    #                 backtrack(row + 1, col, index + 1) or \
    #                 backtrack(row, col - 1, index + 1) or \
    #                 backtrack(row, col + 1, index + 1)
    #
    #         # 恢复当前位置的未访问状态
    #         visited[row][col] = False
    #         return found
    #
    #     # 遍历整个网格，从每个位置开始搜索
    #     for i in range(rows):
    #         for j in range(cols):
    #             if backtrack(i, j, 0):
    #                 return True
    #     return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 使用深度优先搜索算法DFS
        if not board:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, col, index):
            # 如果越界或者当前字符不匹配，返回False
            if row < 0 or row >= rows or col < 0 or col >= cols \
                    or board[row][col] != word[index]:
                return False

            # 如果找到整个单词，返回True
            if index == len(word) - 1:
                return True

            # 标记当前位置已访问
            temp = board[row][col]
            board[row][col] = '#'

            # 递归搜索上、下、左、右四个方向
            found = dfs(row - 1, col, index + 1) or \
                    dfs(row + 1, col, index + 1) or \
                    dfs(row, col - 1, index + 1) or \
                    dfs(row, col + 1, index + 1)

            # 恢复当前位置的字符
            board[row][col] = temp
            return found

        # 遍历整个网络，从每个位置开始搜索
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

# leetcode submit region end(Prohibit modification and deletion)


    
