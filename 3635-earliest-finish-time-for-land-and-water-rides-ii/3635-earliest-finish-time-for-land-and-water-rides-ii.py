from typing import List
from bisect import bisect_left

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        water = sorted(zip(waterStartTime, waterDuration))
        ws = [s for s, _ in water]
        m = len(water)

        prefWater = [0] * m
        prefWater[0] = water[0][1]
        for i in range(1, m):
            prefWater[i] = min(prefWater[i - 1], water[i][1])

        suffWater = [0] * m
        suffWater[-1] = water[-1][0] + water[-1][1]
        for i in range(m - 2, -1, -1):
            suffWater[i] = min(
                suffWater[i + 1],
                water[i][0] + water[i][1]
            )

        land = sorted(zip(landStartTime, landDuration))
        ls = [s for s, _ in land]
        n = len(land)

        prefLand = [0] * n
        prefLand[0] = land[0][1]
        for i in range(1, n):
            prefLand[i] = min(prefLand[i - 1], land[i][1])

        suffLand = [0] * n
        suffLand[-1] = land[-1][0] + land[-1][1]
        for i in range(n - 2, -1, -1):
            suffLand[i] = min(
                suffLand[i + 1],
                land[i][0] + land[i][1]
            )

        ans = float('inf')

        for ls0, ld in zip(landStartTime, landDuration):
            finish = ls0 + ld

            k = bisect_left(ws, finish)

            if k < m:
                ans = min(ans, suffWater[k])

            if k > 0:
                ans = min(ans, finish + prefWater[k - 1])

        for ws0, wd in zip(waterStartTime, waterDuration):
            finish = ws0 + wd

            k = bisect_left(ls, finish)

            if k < n:
                ans = min(ans, suffLand[k])

            if k > 0:
                ans = min(ans, finish + prefLand[k - 1])

        return ans