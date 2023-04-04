# https://leetcode.com/problems/deepest-leaves-sum/description/
# 1302. Deepest Leaves Sum
# Given the root of a binary tree, return the sum of values of its deepest leaves.

# Example 1:
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15

# Example 2:
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root, level, sum_level):

        if len(sum_level)-1 >= level:
            sum_level[level] += root.val
        else:
            sum_level.append(root.val)
        if root.left:
            self.bfs(root.left, level+1, sum_level)
        if root.right:
            self.bfs(root.right, level+1, sum_level)


    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        sum_level = list()
        self.bfs(root,0,sum_level)
        # print(sum_level)
        return sum_level[-1]
