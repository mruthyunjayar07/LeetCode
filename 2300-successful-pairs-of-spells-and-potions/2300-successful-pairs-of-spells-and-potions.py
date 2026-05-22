class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell  # ceiling division

            idx = bisect.bisect_left(potions, min_potion)

            result.append(m - idx)  # all potions from idx onward work

        return result