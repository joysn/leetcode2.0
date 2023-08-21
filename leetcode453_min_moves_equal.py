# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/submissions/
# 453. Minimum Moves to Equal Array Elements
# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.

# Example 1:
# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

# Example 2:
# Input: nums = [1,1,1]
# Output: 0

# Runtime 249ms
# Beats 64.19%of users with Python3
# Memory 17.84MB
# Beats 66.80%of users with Pytho

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()

        # remove duplicates for least numbers
        smallest = nums[0]
        start = 0
        for i in range(1,len(nums)):
            if nums[i] != smallest:
                break
            start += 1

        largest = nums[-1]
        max_cnt = 1
        # Count number of max
        for i in range(len(nums)-2,-1,-1):
            if nums[i] != largest:
                break
            max_cnt += 1

        cnt = 0
        for i in range(start+1, len(nums)):
            if i == start:
                cnt = (nums[i] - nums[start])*max_cnt
            else:
                cnt += nums[i] - nums[start]

        return cnt