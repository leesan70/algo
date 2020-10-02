from collections import deque

class RecentCounter:

    def __init__(self):
        self.stored = deque()

    def ping(self, t: int) -> int:
        self.stored.append(t)
        while t - self.stored[0] > 3000:
            self.stored.popleft()
        return len(self.stored)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)