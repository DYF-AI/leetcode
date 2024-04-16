
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def __init__(self):
        # 搞一个全局遍历进行计数
        self.total_n_queens = 0


    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 和N皇后[51]基本一毛一样
        # 回溯法

        # 初始化棋盘，二位数组
        board = [['.' for _ in range(n)] for _ in range(n)]
        # 列表是使用引用方式
        # total_n_queens = [0]
        def is_valid(board, row, col):
            # 在棋盘board中的row行col列放置皇后，是否合法
            # 只需要判断，上、左上（对角线）、右上（对角线）是否存在皇后

            # col列上面是否存在Q
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # 左上方对角线是否存在
            for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            # 右上方对角线是否存在Q
            for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                if board[i][j] == 'Q':
                    return False

            return True


        def backtrack(board, row):
            # 在第row行放置皇后
            if row == n:
                #total_n_queens[0] += 1
                self.total_n_queens += 1
                return
            for col in range(n):
                # 遍历该行的每个位置
                if is_valid(board, row, col):
                    # 如果当前行是vaild的，放置皇后，进行下一一列判断
                    board[row][col] = 'Q'
                    backtrack(board, row+1)
                    board[row][col] = '.'


        backtrack(board, 0)
        #return total_n_queens[0]
        return self.total_n_queens




# leetcode submit region end(Prohibit modification and deletion)
