# https://leetcode.com/problems/valid-parentheses/
# 20. Valid Parentheses
# Runtime: 101 ms, faster than 5.22% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 26.58% of Python3 online submissions for Valid Parentheses.

class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                st.append(ch)
            elif ch == ")":
                if len(st) > 0 and st[-1] == "(":
                    st = st[:-1]
                else:
                    return False
            elif ch == "}":
                if len(st) > 0 and st[-1] == "{":
                    st = st[:-1]
                else:
                    return False
            elif ch == "]":
                if len(st) > 0 and st[-1] == "[":
                    st = st[:-1]
                else:
                    return False
        if len(st) > 0:
            return False
        return True