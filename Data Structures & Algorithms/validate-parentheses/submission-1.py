class Solution:
    def isValid(self, s: str) -> bool:
        ref_dict = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char not in ref_dict: # check for open parenthese case and push to stack
                stack.append(char)
            else:
                if not stack: # check if any closing bracket has corresponding opening char in stack
                    return False
                if stack[-1] != ref_dict[char]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0

