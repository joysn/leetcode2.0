# https://leetcode.com/problems/find-the-substring-with-maximum-cost/description/
# 2606. Find the Substring With Maximum Cost
# You are given a string s, a string chars of distinct characters and an integer array vals of the same length as chars.

# The cost of the substring is the sum of the values of each character in the substring. The cost of an empty string is considered 0.

# The value of the character is defined in the following way:

# If the character is not in the string chars, then its value is its corresponding position (1-indexed) in the alphabet.
# For example, the value of 'a' is 1, the value of 'b' is 2, and so on. The value of 'z' is 26.
# Otherwise, assuming i is the index where the character occurs in the string chars, then its value is vals[i].
# Return the maximum cost among all substrings of the string s.

# Example 1:
# Input: s = "adaa", chars = "d", vals = [-1000]
# Output: 2
# Explanation: The value of the characters "a" and "d" is 1 and -1000 respectively.
# The substring with the maximum cost is "aa" and its cost is 1 + 1 = 2.
# It can be proven that 2 is the maximum cost.

# Example 2:
# Input: s = "abc", chars = "abc", vals = [-1,-1,-1]
# Output: 0
# Explanation: The value of the characters "a", "b" and "c" is -1, -1, and -1 respectively.
# The substring with the maximum cost is the empty substring "" and its cost is 0.
# It can be proven that 0 is the maximum cost.

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:

        def_dict = dict()
        def_str = "abcdefghijklmnopqrstuvwxyz"
        idx = 1
        for ch in def_str:
            def_dict[ch] = idx
            idx += 1

        giv_dict = dict()
        idx = 0
        for ch in chars:
            giv_dict[ch] = vals[idx]
            idx += 1
        
        l = len(s)
        nums = [None for i in range(l)]
        for i in range(l):
            ch = s[i]
            if ch in giv_dict.keys():
                nums[i] = giv_dict[ch]
            else:
                nums[i] = def_dict[ch]
        print(nums)
        
        max_val = 0
        # for r in range(l):
        #     prev = nums[r]
        #     max_val = max(max_val, prev)
        #     for c in range(r+1,l):
        #         ch_val = nums[c]
        #         curr = max(prev+ch_val, ch_val)
        #         max_val = max(max_val,curr)
        #         prev = curr
        #     # print(cost_arr)
        
        max_val = max(0,nums[0])
        psum = 0
        for i in range(l):
            if psum < 0:
                psum = 0
            psum += nums[i]
            max_val = max(psum, max_val)


        return max_val
