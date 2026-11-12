import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lst = set()
        l, r = 1, max(piles)

        while l <= r:
            mid = (l + r) // 2
            k = mid

            total = 0
            for i in piles:
                total += math.ceil(i / k)

            if total <= h:
                lst.add(k)
                r = mid - 1
            else:
                l = mid + 1

        return min(lst)