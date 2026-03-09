class RecentCounter:

    def __init__(self):
        self.q = []
        self.start = 0

    def ping(self, t: int) -> int:
        self.q.append(t)
        while t-self.q[self.start] > 3000: 
            self.start+=1
        return len(self.q)-self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)