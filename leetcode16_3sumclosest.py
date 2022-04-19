# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0

# Runtime: 357 ms, faster than 53.87% of Python3 online submissions for 3Sum Closest.
# Memory Usage: 14.1 MB, less than 33.28% of Python3 online submissions for 3Sum Closest.

class Solution:
    
    def threeSumClosest(self, numbers: List[int], target: int) -> int:
        
        min_dif = sys.maxsize
        l = len(numbers)

        numbers = sorted(numbers)
        for idx,n in enumerate(numbers):
            lo,hi = idx+1,l-1
            while (lo < hi):
                sum = n + numbers[lo] + numbers[hi]
                if abs(sum - target) < abs(min_dif):
                    min_dif = sum - target

                if sum < target:
                    lo += 1
                else:
                    hi -= 1
                if min_dif == 0:
                    break

        return target + min_dif
        
