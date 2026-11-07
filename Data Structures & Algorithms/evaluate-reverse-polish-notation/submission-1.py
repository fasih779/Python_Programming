class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    res = a + b

                elif token == "-":
                    res = a - b

                elif token == "*":
                    res = a * b

                elif token == "/":
                    res = abs(a) // abs(b)

                    if (a < 0) != (b < 0):
                        res = -res

                stack.append(res)

            else:
                stack.append(int(token))

        return stack[-1]