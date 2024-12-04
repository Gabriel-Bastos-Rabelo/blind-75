class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '[', '{']
        closed = [')', ']', '}']
        stack = []
        for i in s:
            if i in closed:
                indice = closed.index(i)
                if stack and stack[-1] == open[indice]:
                    stack.pop()

                else:
                    return False

            else:
                stack.append(i)

        if stack:
            return False
        return True

