import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1          # tracks the infinite stream
        self.added_back = []      # min-heap for re-added numbers
        self.added_set = set()    # avoid duplicates in heap

    def popSmallest(self) -> int:
        if self.added_back and self.added_back[0] < self.current:
            val = heapq.heappop(self.added_back)
            self.added_set.remove(val)
            return val
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        if num < self.current and num not in self.added_set:
            heapq.heappush(self.added_back, num)
            self.added_set.add(num)