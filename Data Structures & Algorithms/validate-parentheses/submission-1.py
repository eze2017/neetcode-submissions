class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack= []

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1]  == closeToOpen[c]: # check if stack and value is corresponding open bracket
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
