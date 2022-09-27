# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses

# Runtime: 134 ms, faster than 5.02% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 17.8 MB, less than 5.50% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generateStr(pc):
            if pc == 1:
                return ["()"]
                
            fop = []
            top = generateStr(pc-1)
            # add in front ()
            for e in top:
                fop.append("()"+e)
            # add after each (
            for e in top:
                for match in re.finditer("\(", e):
                    idx = match.start()
                    fop.append(e[:idx+1]+"()"+e[idx+1:])
            return fop
        
        return list(set(generateStr(n)))
        