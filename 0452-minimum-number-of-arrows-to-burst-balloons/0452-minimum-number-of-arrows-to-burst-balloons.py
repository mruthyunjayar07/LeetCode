class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])  # sort by END
        arrows = 1
        arrow_pos = points[0][1]
        
        for start, end in points[1:]:
            if start > arrow_pos:        # balloon not hit → shoot new arrow
                arrows += 1
                arrow_pos = end          # shoot at end of current balloon
        
        return arrows