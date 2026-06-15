class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open ={
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack =[]
        #  ( [ { } ] )
        for char in s:
            print(char)
            # is opening bracket
            if char in close_to_open.values():
                stack.append(char)
            else:
                if not stack :
                    return False
                if stack and stack[-1] !=close_to_open[char]:
                    return False
                stack.pop()
                
        return True if not stack else False
        

            
        #     if stack and char in close_to_open:
        #         stack.append(char)
        #     if stack and stack[-1] == close_to_open[char]:
        #         stack.pop()

        # return True if not stack else False
           