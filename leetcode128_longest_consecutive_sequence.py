# https://leetcode.com/problems/longest-consecutive-sequence/
# 128. Longest Consecutive Sequence

# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time. 

# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# [100,4,200,1,3,2]
# [0,3,7,2,5,8,4,6,0,1]

# Runtime: 319 ms, faster than 55.14% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 29.6 MB, less than 16.16% of Python3 online submissions for Longest Consecutive Sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_dict = dict()
        
        if len(nums) == 0:
            return 0
        
        maxl = 1
        for n in nums:
            nums_dict[n] = 1
        #print(nums_dict)
            
        for n in nums:
            if n not in nums_dict:
                continue
            pre = n - 1
            count = 1
            while pre in nums_dict:
                nums_dict[n] += nums_dict[pre]
                del nums_dict[pre]
                if nums_dict[n] > maxl:
                    maxl = nums_dict[n]
                pre -= 1
            #print("for",n,"dict is",nums_dict, "and maxl is",maxl)
        
        return maxl