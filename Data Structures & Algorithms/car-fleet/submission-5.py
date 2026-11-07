class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        fleet = 0

        for pos, sp in cars:
            time = (target - pos) / sp

            if not stack or time > stack[-1]:
                fleet += 1
                stack.append(time)

        return fleet