# https://leetcode.com/problems/diagonal-traverse/description/
# 498. Diagonal Traverse
# Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

# Example 1:
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]

# Example 2:
# Input: mat = [[1,2],[3,4]]
# Output: [1,2,3,4]

# Runtime 6250 ms 
# Beats 5.03% of users with Python3

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        clen = len(mat[0])
        rlen = len(mat)
        total_iter = rlen+clen - 1
        
        op = list()

        for i in range(total_iter):
            if i%2 != 0: 
                for r in range(rlen):
                    if i-r < clen and i-r >= 0:
                        # print(r,i-r,mat[r][i-r])
                        op.append(mat[r][i-r])
            else:
                for c in range(clen):
                    if i-c < rlen and i-c >= 0:
                        # print(i-c,c,mat[i-c][c])
                        op.append(mat[i-c][c])
            # print("for",i,"op is",op)

        # print(op)
        return op


        