# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
# 2089. Find Target Indices After Sorting Array

# You are given a 0-indexed integer array nums and a target element target.

# A target index is an index i such that nums[i] == target.

# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

# Example 1:
# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.

# Example 2:
# Input: nums = [1,2,5,2,3], target = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.

# Example 3:
# Input: nums = [1,2,5,2,3], target = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        count_of_smaller_ele = 0
        count_of_target = 0
        for num in nums:
            if num < target:
                count_of_smaller_ele += 1
            elif num == target:
                count_of_target += 1


        op = []
        start_index = count_of_smaller_ele
        for i in range(count_of_target):
            op.append(start_index)
            start_index += 1
        return op
