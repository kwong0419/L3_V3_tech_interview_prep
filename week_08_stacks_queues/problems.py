# Problems
# 1. Valid Parentheses
# 2. Min Stack
# 3. Implement Queue using Stacks

def valid_parentheses(s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return not stack
# Time Complexity: O(n) where n is the length of the input string
# Space Complexity: O(n) in worst case where all characters are opening brackets

def min_stack():
    class MinStack:
        def __init__(self):
            self.stack = []
            self.min_stack = []

        def push(self, val: int) -> None:
            self.stack.append(val)
            val = min(val, self.min_stack[-1] if self.min_stack else val)
            self.min_stack.append(val)

        def pop(self) -> None:
            self.stack.pop()
            self.min_stack.pop()

        def top(self) -> int:
            return self.stack[-1]

        def getMin(self) -> int:
            return self.min_stack[-1]

    return MinStack()
# Time Complexity: 
# push(): O(1)
# pop(): O(1)
# top(): O(1)
# getMin(): O(1)
# Space Complexity: O(n) where n is the number of elements in the stack (uses two stacks internally, each storing n elements)

def implement_queue_using_stacks():
    class MyQueue:
        def __init__(self):
            self.stack1 = []
            self.stack2 = []

        def push(self, x: int) -> None:
            self.stack1.append(x)

        def pop(self) -> int:
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        
        def peek(self) -> int:
            if not self.stack2:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        
        def empty(self) -> bool:
            return not self.stack1 and not self.stack2

    return MyQueue()
# Time Complexities:
# push(): O(1)
# pop(): Amortized O(1), Worst case O(n)
# peek(): Amortized O(1), Worst case O(n)
# empty(): O(1)
# Space Complexity: O(n) where n is the number of elements in the queue (uses two stacks internally, total space is still O(n))


            