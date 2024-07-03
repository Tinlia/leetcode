class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1: return False

        stack = []
        for p in s:
            if p in ['[', '(', '{']:
                stack.append(p)
            else:
                if len(stack) == 0: return False
                if p == ']' and stack[-1] != '[': return False
                elif p == ')' and stack[-1] != '(': return False
                elif p == '}' and stack[-1] != '{': return False
                stack.pop()  

        return len(stack) == 0  
