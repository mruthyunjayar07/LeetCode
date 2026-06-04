from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n <= 0:
                return 0

            s = str(n)

            @cache
            def dfs(pos, tight, started, prev2, prev1):
                if pos == len(s):
                    return (1, 0) if started else (0, 0)

                limit = int(s[pos]) if tight else 9

                cnt_nums = 0
                cnt_wave = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit

                    if not started and d == 0:
                        c, w = dfs(pos + 1, ntight, False, -1, -1)
                    else:
                        add = 0

                        if prev2 != -1:
                            if (prev1 > prev2 and prev1 > d) or \
                               (prev1 < prev2 and prev1 < d):
                                add = 1

                        c, w = dfs(pos + 1, ntight, True, prev1, d)
                        w += add * c

                    cnt_nums += c
                    cnt_wave += w

                return cnt_nums, cnt_wave

            return dfs(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)