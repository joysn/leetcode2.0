# https://leetcode.com/problems/minimum-time-difference/description/
# 539 Minimum Time Difference
# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

# Example 1:
# Input: timePoints = ["23:59","00:00"]
# Output: 1

# Example 2:
# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0

# Runtime 70 ms
# Beats 70.83% of users with Python3

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convertToMins(t):
            splitT = t.split(":")
            h = int(splitT[0])
            m = int(splitT[1])

            return h*60+m

        op = list()
        for t in timePoints:
            m = convertToMins(t)
            op.append(m)


        op.sort()
        op.append(24*60+op[0])
        print(op)

        mdiff = math.inf
        for idx in range(1,len(op)):
            diff = op[idx] - op[idx-1]
            if diff < mdiff:
                mdiff = diff


        return mdiff
        