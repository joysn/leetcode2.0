# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
# 2177. Find Three Consecutive Integers That Sum to a Given Number
# Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.

# Example 1:
# Input: num = 33
# Output: [10,11,12]
# Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
# 10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].

# Example 2:
# Input: num = 4
# Output: []
# Explanation: There is no way to express 4 as the sum of 3 consecutive integers.


# Runtime: 47 ms, faster than 36.01% of Python3 online submissions for Find Three Consecutive Integers That Sum to a Given Number.
# Memory Usage: 13.9 MB, less than 7.32% of Python3 online submissions for Find Three Consecutive Integers That Sum to a Given Number.

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if num%3 == 0:
            m = int(num/3)
            return [m-1,m,m+1]
        else:
            return []
        