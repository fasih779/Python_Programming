class MinStack:

    def __init__(self):
        self.st = []
        self.mist = []

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.mist or val <= self.mist[-1]:
            self.mist.append(val)

    def pop(self) -> None:
        if self.st[-1] == self.mist[-1]:
            self.mist.pop()

        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mist[-1]