import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap size is k
        heap = []
        # iterate over points
        for point in points:
            # calculate euclidian distance
            distance = (point[0]**2 + point[1]**2) ** .5
            # if distance is smaller than current largest, replace it
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))    
                continue
            if -heap[0][0] >= distance:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, point))

        print( heap)
        return [val for (key, val) in heap]
        # return heap values only