import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            stone_1 = -heapq.heappop(heap)
            stone_2 = -heapq.heappop(heap)

            new_stone = stone_1 - stone_2
            if new_stone:
                heapq.heappush(heap, -new_stone)

        return -heap[0] if len(heap) > 0 else 0
