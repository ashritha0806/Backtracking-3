# Time Complexity : O(m*n*3^l) where m is no. of rows, n is no. of colimns and l is lenght of the word
# Space complexity :O(l) - recurrsion stack space
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : Its taking more time to write a logic to proper running code. 

# Your code here along with comments explaining your approach
# Iterate through every cell on the grid performing DFS whenever a cell matches the first letter of the target word.
# Inside DFS verifying edges and if character matches, then mark the current cell to "#"" to avoid revisting in the current path.
# Recursively search all adjacent directions for the next letter in the word, and restore the cell's original character when returning so it remains available for other paths too.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.direction = [[0,1],[1,0],[0,-1],[-1,0]]
        self.m = len(board)
        self.n = len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, index):
        if index == len(word):
            return True
            #edge case 
        if i < 0 or j < 0 or i >= self.m or j >= self.n or board[i][j] == "#":
            return False

        if board[i][j] != word[index]:
            return False

        board[i][j] = "#"

        #recurse
        for d in self.direction:
            r = d[0] + i
            c = d[1] + j

            if self.dfs(board,r,c,word,index+1):
                return True

        #backtrack
        board[i][j] = word[index]
        return False