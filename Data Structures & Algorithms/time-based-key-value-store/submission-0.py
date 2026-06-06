class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.map[key]) - 1
        ans = ""

        while l <= r:
            mid = (l + r) // 2

            if self.map[key][mid][0] <= timestamp:
                ans = self.map[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans
