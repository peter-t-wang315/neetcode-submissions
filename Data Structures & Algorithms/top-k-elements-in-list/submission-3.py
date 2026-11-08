import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        
        for key, val in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))

            elif heap[0][0] < val:
                heapq.heappop(heap)
                heapq.heappush(heap, (val, key))


        return [key for val, key in heap]
        