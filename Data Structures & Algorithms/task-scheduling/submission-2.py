from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = []
        cooldown = {}
        i = 0

        # turn counts into heap of (# occur, char)
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))

        # index while heap or cooldown are not empty
        while len(heap) > 0 or len(cooldown) > 0:
            if i in cooldown:
                # append it back to heap
                heapq.heappush(heap, cooldown[i])
                # remove i from cooldown
                del cooldown[i]

            # if heap has elements:
            if len(heap) > 0:
                # pop the top
                temp = heapq.heappop(heap)
                if -temp[0] - 1 > 0:
                    # add to cooldown at n+i+1 with (occur+1, char) 
                    cooldown[n+i+1] = (temp[0] + 1, temp[1])
            i+=1
            
        return i