# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/description/
# 2091. Removing Minimum and Maximum From Array

# You are given a 0-indexed array of distinct integers nums.
# There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.
# A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.
# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

# Example 1:
# Input: nums = [2,10,7,5,4,1,8,6]
# Output: 5
# Explanation: 
# The minimum element in the array is nums[5], which is 1.
# The maximum element in the array is nums[1], which is 10.
# We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
# This results in 2 + 3 = 5 deletions, which is the minimum number possible.

# Example 2:
# Input: nums = [0,-4,19,1,8,-2,-3,5]
# Output: 3
# Explanation: 
# The minimum element in the array is nums[1], which is -4.
# The maximum element in the array is nums[2], which is 19.
# We can remove both the minimum and maximum by removing 3 elements from the front.
# This results in only 3 deletions, which is the minimum number possible.

# Example 3:
# Input: nums = [101]
# Output: 1
# Explanation:  
# There is only one element in the array, which makes it both the minimum and maximum element.
# We can remove it with 1 deletion.


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        l = len(nums)
        if l <= 1:
            return l
        
        min_pos_f = 0
        max_pos_f = 0
        min_n = nums[0]
        max_n = nums[0]
        
        for idx in range(l):
            if min_n > nums[idx]:
                min_pos_f = idx
                min_n = nums[idx]
            if max_n < nums[idx]:
                max_pos_f = idx
                max_n = nums[idx]

        min_pos_f += 1
        max_pos_f += 1
        min_pos_e = l - min_pos_f + 1
        max_pos_e = l - max_pos_f + 1
        # print(l, min_pos_f,max_pos_f, min_pos_e, max_pos_e)

        return min(min_pos_f + max_pos_e, min_pos_e + max_pos_f, max(min_pos_f, max_pos_f), max(min_pos_e, max_pos_e))
