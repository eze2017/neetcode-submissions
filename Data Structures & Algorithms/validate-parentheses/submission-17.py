class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []

        for char in s:
            # if closing bracket
            if char in close_to_open:
                # check if stack is empty:
                if not stack or close_to_open[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                # opening bracket 
                stack.append(char)
        
        return True if not stack else False