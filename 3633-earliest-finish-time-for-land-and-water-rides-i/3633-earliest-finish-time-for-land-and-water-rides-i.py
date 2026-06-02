from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        ans = float('inf')

        for i in range(n):
            for j in range(m):
                start_land = landStartTime[i]
                finish_land = start_land + landDuration[i]
                start_water = max(finish_land, waterStartTime[j])
                finish1 = start_water + waterDuration[j]

                start_water2 = waterStartTime[j]
                finish_water2 = start_water2 + waterDuration[j]
                start_land2 = max(finish_water2, landStartTime[i])
                finish2 = start_land2 + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans