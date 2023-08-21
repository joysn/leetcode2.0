# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/
# 452. Minimum Number of Arrows to Burst Balloons
# There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

# Example 1:
# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

# Example 2:
# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

# Example 3:
# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

# Runtime 1147ms
# Beats 80.91%of users with Python3
# Memory 61.96MB
# Beats 93.60%of users with Python3

class Solution:

    def merge(self, p1, p2):
        # print(p1,p2)
        if p1[0] <= p2[0] and p2[0] <= p1[1]:
            fp = p2[0]
            if p1[1] <= p2[1]:
                lp = p1[1]
            else:
                lp = p2[1]
            return [True, [fp,lp]]
        return [False,[]]
        
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points_sorted = sorted(points, key=lambda x: x[0])
        # print(points_sorted)

        l = len(points_sorted)
        op = [points_sorted[0]]
        for i in range(1,l):
            m_op = self.merge(op[-1],points_sorted[i])
            # print(m_op)
            if m_op[1]:
                op.pop()
                op.append(m_op[1])
            else:
                op.append(points_sorted[i])
        # print(op)

        return len(op)