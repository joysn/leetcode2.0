# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
# 1188 ms Beats 5.13%
# Memory 30.64 MB Beats 10.47%

# You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

# The chemistry of a team is equal to the product of the skills of the players on that team.

# Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

# Example 1:
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation: 
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

# Example 2:
# Input: skill = [3,4]
# Output: 12
# Explanation: 
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.

# Example 3:
# Input: skill = [1,1,2,3]
# Output: -1
# Explanation: 
# There is no way to divide the players into teams such that the total skill of each team is equal.

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill_sum = 0
        l = len(skill)
        for i in range(l):
            skill_sum += skill[i]

        team_count = l//2
        each_team_skill_sum = skill_sum//team_count

        chemistry = 0
        player_dict = dict()

        for i in range(l):
            if skill[i] in player_dict.keys():
                player_dict[skill[i]].append(i)
            else:
                player_dict[skill[i]] = [i]

        for i in range(l):
            p1 = i
            p1s = skill[p1]
            if p1s not in player_dict.keys():
                continue
            p2s = each_team_skill_sum - p1s
            # print(p1,p1s,p2s)
            if p2s not in player_dict.keys():
                return -1
            p2 = player_dict[p2s][0]
            if len(player_dict[p1s]) > 1:
                del player_dict[p1s][0]
            else:
                del player_dict[p1s]
            if len(player_dict[p2s]) > 1:
                del player_dict[p2s][0]
            else:
                del player_dict[p2s]
            chemistry += p1s*p2s

        return chemistry

