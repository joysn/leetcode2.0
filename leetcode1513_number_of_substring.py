# https://leetcode.com/problems/number-of-substrings-with-only-1s/description/
# 1513. Number of Substrings With Only 1s
# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

# Example 1:
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

# Example 2:
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.

# Example 3:
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.


# Runtime 61ms
# Beats 82.30%of users with Python3
# Memory 16.81MB
# Beats 84.69%of users with Python3

class Solution:
    def numSub(self, s: str) -> int:

        l = len(s)
        i = 0
        res = 0
        cnt = 0
        while i < l:
            if s[i] != '1':
                res += cnt * (cnt+1)/2
                cnt = 0
                i += 1
            else:
                cnt += 1
                i += 1
        res += cnt * (cnt+1)/2

        return int(res)%(10**9 + 7)
            