# https://leetcode.com/problems/implement-rand10-using-rand7/submissions/
# 470. Implement Rand10() Using Rand7()
# Given the API rand7() that generates a uniform random integer in the range [1, 7], write a function rand10() that generates a uniform random integer in the range [1, 10]. You can only call the API rand7(), and you shouldn't call any other API. Please do not use a language's built-in random API.
# Each test case will have one internal argument n, the number of times that your implemented function rand10() will be called while testing. Note that this is not an argument passed to rand10().

# Example 1:
# Input: n = 1
# Output: [2]

# Example 2:
# Input: n = 2
# Output: [2,8]

# Example 3:
# Input: n = 3
# Output: [3,8,10]

# Runtime 242ms
# Beats 72.50%of users with Python3
# Memory 19.16MB
# Beats 22.20%of users with Python3

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """

        c = (rand7()-1)*7 + rand7() - 1
        if c < 40:
            return c%10 + 1
        return self.rand10()