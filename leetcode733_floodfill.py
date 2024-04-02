# https://leetcode.com/problems/flood-fill/
# 733. Flood Fill

# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

 

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made to the image.

# Runtime 60 ms Beats 91.03% of users with Python3
# Memory 16.68 MB Beats 75.95% of users with Python3


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        length = len(image)
        breadth = len(image[0])
        src_color = image[sr][sc]

        def dfs(r,c):
            # print(r,c)
            if image[r][c] != src_color:
                return
            if image[r][c] == color:
                return
            
            image[r][c] = color
            if r-1 >= 0:
                dfs(r-1,c)
            if c-1 >= 0:
                dfs(r,c-1)
            if r+1 <= length-1:
                dfs(r+1,c)
            if c+1 <= breadth-1:
                dfs(r,c+1)
            
        dfs(sr,sc)
        return image
        
