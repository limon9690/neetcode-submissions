class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for cords in points:
            dist = -math.sqrt(cords[0] ** 2 + cords[1] ** 2)

            heapq.heappush(heap, (dist, cords[0], cords[1]))

            if len(heap) > k:
                heapq.heappop(heap)

        
        return [[pair[1], pair[2]] for pair in heap]