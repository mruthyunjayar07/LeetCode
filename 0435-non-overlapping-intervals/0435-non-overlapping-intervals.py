class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])  # sort by END time
        removes = 0
        prev_end = float('-inf')
        
        for start, end in intervals:
            if start < prev_end:       # overlaps → remove current
                removes += 1
            else:                      # no overlap → keep it
                prev_end = end
        
        return removes