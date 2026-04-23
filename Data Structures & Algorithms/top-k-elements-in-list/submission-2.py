class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] = count[num] + 1

        res = []

        for i in range(k):
            top = float('-inf')
            curr = -1
            for key, value in count.items():
                if value > top:
                    curr = key
                    top = value

            res.append(curr)
            del count[curr]

        return res