# https://leetcode.com/problems/min-stack/submissions/1166476828/

# 155. Min Stack
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 
# Constraints:
# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

# Runtime 40 ms
# Beats 99.50% of users with Python3

# Memory 20.82 MB
# Beats 58.96% of users with Python3

class MinStack:
    minstack = list()
    minPosStack = list()
    l = 0

    def __init__(self):
        self.minstack = list()
        self.minPosStack = list()
        self.l = 0
        

    def push(self, val: int) -> None:
        self.minstack.append(val)
        self.l += 1
        if self.l == 1: # first element inserted
            self.minPosStack.append(self.l-1)
        else: #previous element was present
            if self.minstack[self.minPosStack[-1]] > val:
                self.minPosStack.append(self.l - 1)
            else:
                temp = self.minPosStack.pop()
                self.minPosStack.append(self.l - 1)
                self.minPosStack.append(temp)
        

    def pop(self) -> None:
        self.minPosStack.remove(len(self.minstack)-1)
        self.l -= 1
        return self.minstack.pop()
        

    def top(self) -> int:
        return self.minstack[-1]
        

    def getMin(self) -> int:
        return self.minstack[self.minPosStack[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
