# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = []
# Output: []

# Example 3:
# Input: nums = [0]
# Output: []

# Runtime: 1506 ms, faster than 39.66% of Python3 online submissions for 3Sum.
# Memory Usage: 19.2 MB, less than 7.25% of Python3 online submissions for 3Sum.

class Solution:
    
    def sum2(self,numbers, target):
        if len(numbers) == 0:
            return

        op = []
        sumdict = dict()
        for num in numbers:
            remaining = target - num
            if num in sumdict:
                op.append(tuple(sorted([num,remaining])))
                del sumdict[num]
            else:
                sumdict[remaining] = 0 
        return [list(x) for x in op]

    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        target = 0
        if len(numbers) <= 2:
            return []
        
        num_count = dict()
        for e in numbers:
            if e in num_count.keys():
                num_count[e] += 1
            else:
                num_count[e] = 1
                
        op = set()
        for idx,n in enumerate(numbers):
            if num_count[n] != 0:
                num_count[n] = 0
                remaining = target - n
                res = self.sum2(numbers[:idx]+numbers[idx+1:],remaining)
                if len(res) > 0:
                    for l in res:
                        l.append(n)
                        op.add(tuple(sorted(l)))
                    # print(res)
        return [list(x) for x in op]
        
