class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value 
        self.k = k 
        self.q = deque()

    def consec(self, num: int) -> bool:
        
        if len(self.q) == self.k: 
            self.q.popleft()
        self.q.append(num)
        if num != self.value: 
            self.q.clear()
        return len(self.q) == self.k
        




# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)