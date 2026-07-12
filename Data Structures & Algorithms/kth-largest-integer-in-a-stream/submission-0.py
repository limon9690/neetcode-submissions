class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap = []
        #heapq.heapify(self.max_heap)
        for n in nums:
            heapq.heappush(self.max_heap, -n)
        print(self.max_heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.max_heap, -val)
        res = -1
        temp = []

        i = self.k
        while i > 0:
            temp.append(heapq.heappop(self.max_heap))
            i -= 1

        res = temp[-1]

        while temp:
            heapq.heappush(self.max_heap, temp.pop())

        return -res
        
