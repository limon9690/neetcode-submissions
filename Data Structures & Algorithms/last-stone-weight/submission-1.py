class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue

            larger = x if x > y else y
            smaller = y if x > y else x

            heapq.heappush(heap, -(larger-smaller))

        
        return -heap[0] if len(heap) == 1 else 0