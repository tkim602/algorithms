# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# Examples: Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Input: s = "3[a2[c]]"
# Output: "accaccacc"


# method 1: Using recursion
class Solution:
    def decodeString(self, s: str) -> str:
        def helper(index):
            result = ""
            num = 0

            while index < len(s):
                char = s[index]

                if char.isdigit():
                    # initialize the multiplier 
                    num = num * 10 + int(char)
                elif char == '[':
                    # if '[' is encounterd, recursion happens so that it can handle the charcters inside
                    index, decoded_string = helper(index + 1)
                    result += num * decoded_string
                    num = 0  # clear num (the multiplier)
                elif char == ']':
                    # if '[' is encountered, return the result and the current index
                    return index, result
                else:
                    # += char to the result
                    result += char

                index += 1

            return result

        # recurion from the outside
        return helper(0)[1]

# method 2: without using recursion, but stack
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


# Both methods, with/without recursion, have the time complexity of O(n). 




