# 2225. Find Players With Zero or One Losses
# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

# Example 1:
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

# Example 2:
# Input: matches = [[2,3],[1,3],[5,4],[6,4]]
# Output: [[1,2,5,6],[]]
# Explanation:
# Players 1, 2, 5, and 6 have not lost any matches.
# Players 3 and 4 each have lost two matches.
# Thus, answer[0] = [1,2,5,6] and answer[1] = [].

# Runtime: 2526 ms, faster than 61.61% of Python3 online submissions for Find Players With Zero or One Losses.
# Memory Usage: 70 MB, less than 18.73% of Python3 online submissions for Find Players With Zero or One Losses.

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        score_dict = dict()
        players = set()
        
        for res in matches:    
            players.add(res[0])
            players.add(res[1])
            if res[1] in score_dict.keys():
                score_dict[res[1]] += 1
            else:
                score_dict[res[1]] = 1
                
        
        no_loss_players = sorted(list(players - set(score_dict.keys())))
        # print(no_loss_players)
        
        one_loss_players = list()
        for pl in score_dict.keys():
            if score_dict[pl] == 1:
                one_loss_players.append(pl)
        
        # print(one_loss_players)
        return [no_loss_players,sorted(one_loss_players)]
                    