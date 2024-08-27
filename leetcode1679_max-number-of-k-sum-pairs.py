# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

# 1252 ms Beats 5.02%
# Memory 30.09 MB Beats 5.70%


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        l = len(nums)
        nums_dict = dict()
        for i in range(l):
            if nums[i] in nums_dict.keys():
                nums_dict[nums[i]].append(i)
            else:
                nums_dict[nums[i]]=[i]

        count = 0
        for i in range(l):
            n1 = nums[i]
            if n1 not in nums_dict.keys():
                continue
            n2 = k - n1
            if n2 == n1 and len(nums_dict[n1]) == 1:
                continue
            if n2 in nums_dict.keys():
                count += 1
                if len(nums_dict[n1]) < 2:
                    del nums_dict[n1]
                else:
                    del nums_dict[n1][0]
                if len(nums_dict[n2]) < 2:
                    del nums_dict[n2]
                else:
                    del nums_dict[n2][0]
            
        return count
                
        
