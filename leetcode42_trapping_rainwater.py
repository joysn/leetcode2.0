
# https://leetcode.com/problems/trapping-rain-water/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


# Runtime: 198 ms, faster than 65.19% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 16 MB, less than 81.94% of Python3 online submissions for Trapping Rain Water.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        left_max = [0 for i in range(n)]
        right_max = [0 for i in range(n)]
        
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(height[i], left_max[i-1])
            
        # print(height)
        # print(left_max)
        
        right_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            right_max[i] = max(height[i],right_max[i+1])
            
        # print(right_max)
        ans = 0
        for i in range(1,n-1):
            ans += min(left_max[i], right_max[i]) - height[i]
            
        return ans
        
        
        