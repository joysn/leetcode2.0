# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
# 387. First Unique Character in a String

# Runtime: 317 ms, faster than 19.46% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.2 MB, less than 16.57% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        chDict = {}
        l = len(s)
        for i in range(l):
            ch = s[i]
            if ch in chDict.keys():
                chDict[ch] = -1
            else:
                chDict[ch] = i
                
            
        # print(chDict)
        ans = -1
        for k in chDict.keys():
            v = chDict[k]
            if v != -1:
                if ans == -1:
                    ans = v
                else:
                    ans = min(ans, v)
        
        return ans