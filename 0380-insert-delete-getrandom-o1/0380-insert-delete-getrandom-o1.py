class RandomizedSet:

    def __init__(self):
        self.nums = []           # list for O(1) random access
        self.idx_map = {}        # val → index in nums

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False
        last = self.nums[-1]
        i = self.idx_map[val]
        self.nums[i] = last
        self.idx_map[last] = i
        self.nums.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)