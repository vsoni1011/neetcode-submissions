class MinStack:

    def __init__(self):
        self.st = []
        


    def push(self, val: int) -> None:
        curr_min=val
        if self.st:
            curr_min = min(val, self.st[-1][1])
        self.st.append((val, curr_min))
        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]
