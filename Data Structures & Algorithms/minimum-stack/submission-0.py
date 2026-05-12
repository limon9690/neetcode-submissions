class MinStack:

    def __init__(self):
        self.main = []
        self.min = []

    def push(self, val: int) -> None:
        self.main.append(val)

        if self.min and val > self.min[-1]:
            return

        self.min.append(val)
        

    def pop(self) -> None:
        x = self.main.pop()

        if x == self.min[-1]:
            self.min.pop()


    def top(self) -> int:
        return self.main[-1]


    def getMin(self) -> int:
        return self.min[-1]
        
