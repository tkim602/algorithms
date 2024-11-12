# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Example: 
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        if k > 0: 
            stack = stack[:-k]
        else: 
            stack        
        result = ''.join(stack).lstrip('0')
        
        return result if result else '0'

# Given num "1432219" and k = 3, stack and k > 0 and stack[-1] > digit, this line checks three conditions:
# 1. stack ensures that stack is not empty, 
# 2. k > 0 ensures that there are digits left to remove 
# 3. stack[-1] > digit checks if the last digit in the stack is larger than the current digit

# Walkthough with the example: 
# - Initialize the stack 
# - Process 1, stack becomes [1]
# - Process 4, stack becomes [1, 4]
# - Process 3, stack[-1] > digit (4 > 3) and k > 0, thus, pop 4 and k becomes 2. push 3, now stack becomes [1, 3]
# - Process 2, stack[-1] > digit (3 > 2) and k > 0, thus pop 3 and k becomes 1. push 2, now stack becomes [1, 2]
# - Repeat and the stack finally becomes [1, 2, 1, 9]. Therefore, result would be 1219.  
