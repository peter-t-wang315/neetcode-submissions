class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 0:
            return 0

        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleetStack = []
        fleetStack.append(cars[0])

        for car in cars:
            if (target - fleetStack[-1][0]) / fleetStack[-1][1] < (target - car[0]) / car[1]:
                fleetStack.append(car)

        return len(fleetStack)
