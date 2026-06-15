class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close= {
            "[":"]",
            "{":"}",
            "(":")"
             }
        stack = []
        for c in s:
            if c in open_to_close:
                stack.append(c)
            else:
                # if stack is not empty 
                if not stack or open_to_close[stack.pop()] != c:
                    return False
        return len(stack)== 0