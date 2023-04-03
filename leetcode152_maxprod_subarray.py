# https://leetcode.com/problems/maximum-product-subarray/description/
# 152. Maximum Product Subarray
# Given an integer array nums, find a 
# subarray that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# Example 
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # maxProd = nums[0]

        # for idx in range(1,len(nums)):
        #     prod = nums[idx]*nums[idx-1]
        #     if nums[idx] < prod:
        #         nums[idx] = prod
        #     if maxProd < nums[idx]:
        #         maxProd = nums[idx]
        # print(nums)

        maxProd = float('-inf')
        sz = len(nums)
        l = 1
        r = 1

        for i in range(sz):
            l *= nums[i]
            r *= nums[sz-i-1]
            maxProd = max(l,r,maxProd)
            if l == 0:
                l = 1
            if r == 0:
                r = 1

        return maxProd
