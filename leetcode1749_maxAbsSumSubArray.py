# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
# 1749. Maximum Absolute Sum of Any Subarray
# You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

# Return the maximum absolute sum of any (possibly empty) subarray of nums.

# Note that abs(x) is defined as follows:

# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
 

# Example 1:
# Input: nums = [1,-3,2,3,-4]
# Output: 5
# Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

# Example 2:
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # max_sum = abs(nums[0])
        # for i in range(l):
        #     c_sum = nums[i]
        #     max_sum = max(abs(c_sum), max_sum)
        #     for j in range(i+1,l):
        #         c_sum += nums[j]
        #         max_sum = max(abs(c_sum), max_sum)
        # return max_sum

        max_abs_sum = 0
        cur_max, cur_min = 0, 0
        for num in nums:
            cur_max = max(num, cur_max + num)
            cur_min = min(num, cur_min + num)
            max_abs_sum = max(max_abs_sum, abs(cur_min), abs(cur_max))
        return max_abs_sum
