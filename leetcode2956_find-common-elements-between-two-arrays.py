# https://leetcode.com/problems/find-common-elements-between-two-arrays
# Runtime 123 ms Beats 86.82%
# Memory 16.52 MB Beats 39.06%

# You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

# answer1 : the number of indices i such that nums1[i] exists in nums2.
# answer2 : the number of indices i such that nums2[i] exists in nums1.
# Return [answer1,answer2].

# Example 1:
# Input: nums1 = [2,3,2], nums2 = [1,2]
# Output: [2,1]

# Example 2:
# Input: nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]
# Output: [3,4]
# The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.
# The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

# Example 3:
# Input: nums1 = [3,4,2,3], nums2 = [1,5]
# Output: [0,0]
# Explanation: No numbers are common between nums1 and nums2, so answer is [0,0].

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        l1 = len(nums1)
        l2 = len(nums2)

        nums1_dict = dict()
        nums2_dict = dict()

        for i in range(l1):
            if nums1[i] not in nums1_dict.keys():
                nums1_dict[nums1[i]] = 1

        ans2 = 0
        for i in range(l2):
            if nums2[i] not in nums2_dict.keys():
                nums2_dict[nums2[i]] = 1
            if nums2[i] in nums1_dict.keys():
                ans2 += 1
        
        ans1 = 0
        for i in range(l1):
            if nums1[i] in nums2_dict.keys():
                ans1 += 1

        return (ans1, ans2)
        
        
