# https://leetcode.com/problems/house-robber/submissions/
# 198. House Robber
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can 
# rob tonight without alerting the police.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# Runtime: 54 ms, faster than 26.66% of Python3 online submissions for House Robber.
# Memory Usage: 13.9 MB, less than 18.83% of Python3 online submissions for House Robber.

class Solution:
    def maxHouseRob(self,idx,n,nums,memo):
        if idx == n-1:
            return nums[idx]

        if memo[idx] != -1:
            return memo[idx]
        if idx == n-2:
            memo[idx] = max(nums[idx], nums[idx+1])
            return memo[idx]
        
        memo[idx] = max((nums[idx]+self.maxHouseRob(idx+2,n,nums,memo)),(self.maxHouseRob(idx+1,n,nums,memo)))
        return memo[idx]
    
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # memo = [-1 for i in range(n)]
        # return self.maxHouseRob(0,n,nums, memo)
    
        if n == 0:
            return 0

        if n == 1:
            return nums[n-1]

        dp = [-1 for i in range(n)]
        dp[0] = nums[0]
        for i in range(1,n):
            if i-2 >= 0:
                ans = max(dp[i-2]+nums[i], dp[i-1])
            else:
                ans = max(nums[i],dp[i-1])
            dp[i] = ans
        return dp[n-1]
        