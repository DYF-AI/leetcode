# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 二维数组+回溯法
        # 思路：两层遍历

        # 初始化棋盘 二位数组
        board = [['.' for _ in range(n)] for _ in range(n)]
        result = []

        def is_valid(board, row, col):
            # 检查该列是否存在皇后
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # 检查左上方是否有皇后
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # 检右上方是否有皇后
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False
            return True



        def backtrack(board, row):
            # 对第row行放置皇后
            if row == n:
                # 满足条件
                result.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_valid(board, row, col):
                    # 做选择：在当前位置做选择
                    board[row][col] = 'Q'
                    # 递归
                    backtrack(board, row+1)
                    # 回溯
                    board[row][col] = '.'

        backtrack(board, 0)
        return result



# leetcode submit region end(Prohibit modification and deletion)
