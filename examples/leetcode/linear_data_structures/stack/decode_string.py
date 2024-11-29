
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# Examples: Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# This is the same example from the recursion section. This algorithm has a runtime of O(n) because you iterate through the string once to return a result string. 

class Solution:
    def decodeString(self, s: str) -> str:
        # am empty stack to decode the string input
        stack = []

        # Iterate through each character of the string
        for char in s:
            # if it is not ], push it to the stack
            if char != "]":
                stack.append(char)
            # Else, decode    
            else: 
                curr_str = ""
                while stack[-1] != "[":
                    # pop characters until '['
                    curr_str = stack.pop() + curr_str
                # pop '[' from the stack so that you now have the charcters only
                stack.pop() 

                curr_num = ""
                while stack and stack[-1].isdigit():
                    # pop digits to form the multipler i
                    curr_num = stack.pop() + curr_num
                # decode the string by iterating it i times 
                curr_str = int(curr_num) * curr_str
                # push the decoded string to the stack
                stack.append(curr_str)
        # join all elements in the stack to make the final decoded string
        return "".join(stack)





