class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # total boat count, l r pointers
        total_boats = 0
        l = 0
        r = len(people) - 1
        people.sort()

        while l <= r:
            # if l + r > limit: move r, add one to total count
            if people[l] + people[r] > limit:
                r -= 1
                total_boats += 1
            # else: move l and r and add one to toal count
            else:
                l += 1
                r -= 1
                total_boats += 1
        
        return total_boats