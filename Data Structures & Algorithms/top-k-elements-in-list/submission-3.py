class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] = count[num] + 1

        heap = []

        for key, value in count.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        while heap:
            res.append(heapq.heappop(heap)[1])

        return res