import heapq
class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left_max_heap, -num)

        left_max_num = -heapq.heappop(self.left_max_heap)
        heapq.heappush(self.right_min_heap, left_max_num)
        if len(self.left_max_heap) < len(self.right_min_heap):
            x = -heapq.heappop(self.right_min_heap)
            heapq.heappush(self.left_max_heap, x)
        

    def findMedian(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (-self.left_max_heap[0] + self.right_min_heap[0])/2
        else:
            return -self.left_max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()