# https://leetcode.com/problems/ones-and-zeroes/description/
# 474. Ones and Zeroes

# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.


# Example 1:
# Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

# Example 2:
# Input: strs = ["10","0","1"], m = 1, n = 1
# Output: 2
# Explanation: The largest subset is {"0", "1"}, so the answer is 2.


class Solution:

    def count(self, strs):
        count_dict = dict()
        for s in strs:
            if s not in count_dict.keys():
                zeroc = s.count('0')
                onec = s.count('1')
                count_dict[s]=(zeroc,onec)  
        return count_dict

    def fm(self,strlist,m,n,count_dict):
        # print("Iterate", m, n, strlist)
        if m == 0 and n == 0:
            return 0

        mopl = 0
        for idx in range(0,len(strlist)):
            s = strlist[idx]
            zc = count_dict[s][0]
            oc = count_dict[s][1]
            if m >= zc and n >= oc:
                strlist.remove(s)
                opl = self.fm(strlist,m-zc,n-oc,count_dict)
                # print("Op",opl+1)
                if mopl < opl+1:
                    mopl = opl+1
                strlist.insert(idx,s)
        return mopl

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count_dict = dict()
        count_dict = self.count(strs)
        # print(count_dict)

        fop = self.fm(strs,m,n,count_dict)
        # print("Final Op",fop)


        return fop

# Runtime 1296 ms
# Beats 92.89% of users with Python3

class Solution:
    def count(self, strs):
        count_dict = dict()
        for s in strs:
            if s not in count_dict.keys():
                zeroc = s.count('0')
                onec = s.count('1')
                count_dict[s]=(zeroc,onec)  
        return count_dict


    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count_dict = dict()
        count_dict = self.count(strs)


        @cache
        def dp(m,n,idx):
            if m < 0 or n < 0:
                return -math.inf
            if idx == len(strs):
                return 0

            return max(dp(m,n,idx+1), 1 + dp(m-count_dict[strs[idx]][0], n-count_dict[strs[idx]][1], idx+1))
            
        fop = dp(m,n,0)
        # print("Final Op",fop)

        return fop


        