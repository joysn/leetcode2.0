# https://leetcode.com/problems/count-number-of-homogenous-substrings/submissions/
# 1759. Count Number of Homogenous Substrings
# Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
# A string is homogenous if all the characters of the string are the same.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "abbcccaa"
# Output: 13
# Explanation: The homogenous substrings are listed as below:
# "a"   appears 3 times.
# "aa"  appears 1 time.
# "b"   appears 2 times.
# "bb"  appears 1 time.
# "c"   appears 3 times.
# "cc"  appears 2 times.
# "ccc" appears 1 time.
# 3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

# Example 2:
# Input: s = "xy"
# Output: 2
# Explanation: The homogenous substrings are "x" and "y".

# Example 3:
# Input: s = "zzzzz"
# Output: 15

# Runtime 134ms
# Beats 62.83%of users with Python3
# Memory 17.44MB
# Beats 39.79%of users with Python3

class Solution:
    def countHomogenous(self, s: str) -> int:

        l = len(s)

        res = 0
        cnt = 1
        i = 1
        while i < l:
            if s[i] != s[i-1]:
                res += cnt*(cnt+1)/2
                cnt = 1
            else:
                cnt += 1
            i += 1

        res += cnt*(cnt+1)/2

        return int(res) % (10 ** 9 + 7)
