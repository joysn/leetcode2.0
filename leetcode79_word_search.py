# https://leetcode.com/problems/word-search/
# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Runtime: 4781 ms, faster than 91.08% of Python3 online submissions for Word Search.
# Memory Usage: 14 MB, less than 53.46% of Python3 online submissions for Word Search.

class Solution:    
    def dfs(self,board,row,col,word,wordidx):
        if wordidx == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0])\
            or board[row][col] != word[wordidx]:
            return False
        
        temp = board[row][col]
        board[row][col] = '#'
        
        found = self.dfs(board,row+1,col,word,wordidx+1)\
            or self.dfs(board,row-1,col,word,wordidx+1)\
            or self.dfs(board,row,col-1,word,wordidx+1)\
            or self.dfs(board,row,col+1,word,wordidx+1)
        
        board[row][col] = temp
        return found

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        for r in range(rows):
            for c in range(cols):
                if self.dfs(board,r,c,word,0):
                    return True
                
        return False
        