class Solution(object):
    def isValid(self, s):
        stack=[]
        closebracket_map={'}':'{',']':'[',')':'('}
        for c in s:
            if c in closebracket_map:    # close bracket 
                if (stack and stack[-1]==closebracket_map[c]):
                    stack.pop()

                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False