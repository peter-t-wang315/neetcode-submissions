class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for asteroid in asteroids:
            if asteroid > 0:
                res.append(asteroid)
            else:
                destroyed = False
                while len(res) > 0:
                    peek = res[-1]
                    # If peek is positive and larger than our current asteroid is 
                    if peek < 0:
                        destroyed = True
                        res.append(asteroid)
                        break
                    elif peek > abs(asteroid):
                        destroyed = True
                        break
                    elif peek < abs(asteroid):
                        res.pop()
                    else:
                        destroyed = True
                        x = res.pop()
                        break
                if not destroyed:
                    res.append(asteroid)

        return res
                