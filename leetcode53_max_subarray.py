# https://leetcode.com/problems/maximum-subarray/description/
# 53. Maximum Subarray
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        l = len(nums)
        maxNum = nums[0]
        sumArray = [None for c in range(l)]

        for i in range(l):
            if i == 0:
                sumArray[i] = nums[i]
            else:
                sumArray[i] = max(nums[i],sumArray[i-1]+nums[i])
            if maxNum < sumArray[i]:
                maxNum = sumArray[i]


        # for r in sumArray:
        #     print(r)
        return maxNum
