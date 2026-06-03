class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if self.can_finish_within_hours(piles, h, mid):
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        
        return ans


    def can_finish_within_hours(self, piles, h, k):
        total = 0

        for pile in piles:
            total += math.ceil(pile / k)

        return total <= h