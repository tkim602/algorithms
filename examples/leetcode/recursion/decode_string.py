# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# Examples: Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
                
            else: 
                curr_str = ""
                while stack[-1] != "[":
                    curr_str = stack.pop() + curr_str
                stack.pop()

                curr_num = ""
                while stack and stack[-1].isdigit():
                    curr_num = stack.pop() + curr_num
                
                curr_str = int(curr_num) * curr_str
                stack.append(curr_str)

        return "".join(stack)
