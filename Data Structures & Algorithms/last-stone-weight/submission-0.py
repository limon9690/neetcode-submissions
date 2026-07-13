class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = - heapq.heappop(max_heap)
            y = - heapq.heappop(max_heap)

            if x == y:
                continue

            largest = x if x > y else y
            smallest = x if x < y else y

            new_stone = largest - smallest
            heapq.heappush(max_heap, -new_stone)

        
        return - max_heap[0] if max_heap else 0