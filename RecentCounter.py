from collections import deque  

class RecentCounter:

    def __init__(self):
        self.requests = deque() 

    def ping(self, t: int) -> int:
        self.requests.append(t) 

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)

n = int(input("Kitne pings lena hai: "))

counter = RecentCounter()

for _ in range(n):
    t = int(input("Enter ping time (t): "))
    print("Current count:", counter.ping(t))
