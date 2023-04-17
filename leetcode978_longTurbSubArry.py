# https://leetcode.com/problems/longest-turbulent-subarray/description/
# 978. Longest Turbulent Subarray

# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
 
# Example 1:
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

# Example 2:
# Input: arr = [4,8,12,16]
# Output: 2

# Example 3:
# Input: arr = [100]
# Output: 1

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        l = len(arr)

        if l <= 1:
            return l

        max_cnt = 0
        curr_cnt = 1
        prev = 0
        curr = 0

        for i in range(l-1):
            if arr[i] < arr[i+1]:
                curr = 1
            elif arr[i] > arr[i+1]:
                curr = 2
            else:
                curr = 0

            if prev > 0 and curr > 0 and prev != curr:
                curr_cnt += 1
            elif curr > 0 and prev != curr:
                curr_cnt = 2
            elif curr == 0:
                # print("I am same")
                curr_cnt = 1
            elif prev == curr:
                curr_cnt = 2
            if curr_cnt > max_cnt:
                max_cnt = curr_cnt
            
            # print("Curr count is", curr_cnt, "Max cnt is", max_cnt)
            prev = curr
        
        return max_cnt
