# Time Complexity : O(n!)
# Space complexity :O(n^2): board + O(n):recursion stack = O(n^2)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Made some synatx errors and took some time to debug those.

# Your code here along with comments explaining your approach
# Used a backtracking algorithm to place one queen per row, recursively moving to the next row only if a valid column is found.
# Before placing a queen validating safety by checking if the column or diagonals exist in the hash sets.
# When backtracking, remove the queen and clear its coordinates from the tracking sets, once all rows are filled, convert the boolean grid into strings and save it.

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        board = []

        #creating board with all values as fasle
        for i in range(n):
            board.append([False] * n)

        self.helper(board, 0, n)
        return self.result

    def helper(self, board, row, n):
        if row == n:
            sublist = []
            for i in range(n):
                #string builder
                sb = []
                for j in range(n):
                    if board[i][j]:
                        sb.append("Q")
                    else:
                        sb.append(".")
                sublist.append("".join(sb))
            self.result.append(sublist)
            return

        for col in range(n):
            if self.isSafe(board, row, col, n):
                #action
                board[row][col] = True
                #reucrsion
                self.helper(board, row+1, n)
                #backtracking
                board[row][col] = False

    def isSafe(self,board, row, col, n):

        #column
        for i in range(row):
            if board[i][col]:
                return False

        #diagonal up left
        r,c = row, col

        while r >= 0 and c >= 0:
            if board[r][c]:
                return False
            r -= 1
            c -= 1

        #diagonal up right
        r,c = row, col

        while r >= 0 and c < n:
            if board[r][c]:
                return False
            r -= 1
            c += 1
            
        return True