# Given an input string s and a pattern p, implement regular expression matching 
# with support for '.' and '*' where: 

# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Base cases
        if p == "" and s == "":
            # If both pattern and string are empty, they match.
            return True
        if p == "" and s != "":
            # If pattern is empty but string is not, no match is possible.
            return False

        star = False # tell if the current character is followed by *
        char = p[0]  # first character of the pattern        
        
        # Check if the second character in the pattern is '*'
        if len(p) >= 2 and p[1] == "*":
            star = True # if true, then set the star to True
        
        # Else, if there is no '*', we should match the first characters directly
        if not star:
            if s == "":
                # If string is empty, no possible matches without '*'
                return False
            if (char == ".") or (char == s[0]):
                # If char is '.' or it matches the first character of s, check the rest starting from index 1 to the end
                return self.isMatch(s[1:], p[1:])
            # If char does not match s[0] and it’s not '.', return False
            return False
        
        # char is followed by '*', which can match zero or more occurrences of char
        if len(p) >= 4 and p[0:2] == p[2:4]:
            # for cases like 'a*a*a*', skip reduandant '*' pairs
            return self.isMatch(s, p[2:])

        if s == "":
            # If string is empty, skip and move to the next part of the pattern
            return self.isMatch(s, p[2:])

        for i in range(0, len(s)+1):
            if (char == ".") or (s[:i] == char*i):
                # If char is '.' or char repeated i times in s[:i]
                if self.isMatch(s[i:], p[2:]):
                    # recursion to check the rest of s and pattern
                    return True
            else:
                # If s[:i] does not match char repeated i times, break the loop
                return False
        
        # if no matches possible, return False
        return False
