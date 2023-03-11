# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
# 653. Two Sum IV - Input is a BST

# Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

# Example 1:
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Example 2:
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -104 <= Node.val <= 104
# root is guaranteed to be a valid binary search tree.
# -105 <= k <= 105

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    tree_dict = dict()

    def dfs(self,r):
        if r!= None:
            if r.val not in self.tree_dict.keys():
                self.tree_dict[r.val] = 1
            else:
                self.tree_dict[r.val] += 1
            self.dfs(r.left)
            self.dfs(r.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.tree_dict = dict()
        self.dfs(root)
        print(self.tree_dict)

        for num1 in self.tree_dict.keys():
            num2 = k - num1
            if num2 in self.tree_dict.keys():
                if num1 != num2:
                    return True
                else:
                    if self.tree_dict[num1] > 1:
                        return True

        return False


        
