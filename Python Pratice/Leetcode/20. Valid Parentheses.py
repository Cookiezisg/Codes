class Solution:
    def isValid(self, s: str):
        the_stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                the_stack.append(i)
            elif the_stack ==[]:
                return False
            elif i == ')' and the_stack[-1] == '(':
                del the_stack[-1]
            elif i == ']' and the_stack[-1] == '[':
                del the_stack[-1]
            elif i == '}' and the_stack[-1] == '{':
                del the_stack[-1]
            else:
                return False
        if the_stack == []:
            return True
        else:
            return False

solution = Solution()
print(solution.isValid("()[]{}"))