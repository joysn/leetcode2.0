# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# 1647. Minimum Deletions to Make Character Frequencies Unique
# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1. 

# Example 1:
# Input: s = "aab"
# Output: 0
# Explanation: s is already good.

# Example 2:
# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

# Example 3:
# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


# Runtime: 480 ms, faster than 17.92% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.
# Memory Usage: 14.8 MB, less than 94.39% of Python3 online submissions for Minimum Deletions to Make Character Frequencies Unique.

class Solution:
    def minDeletions(self, s: str) -> int:
            
        
        freq = {}
        
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1
                
        freq_arr = sorted(freq.values(),reverse = True)
        # print(freq_arr)
        count = 0
        for i in range(1,len(freq_arr)):
            if freq_arr[i] >= freq_arr[i-1]:
                if freq_arr[i-1] == 0:
                    count += freq_arr[i]
                    freq_arr[i] = 0
                else:
                    count += freq_arr[i] - freq_arr[i-1] + 1
                    freq_arr[i] -= freq_arr[i] - freq_arr[i-1] + 1
        
        print(freq_arr)
        return count