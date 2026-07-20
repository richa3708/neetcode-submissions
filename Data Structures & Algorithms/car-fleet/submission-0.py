class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair positions with speeds and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd
            # If this car takes longer, it's a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Else, it joins the fleet ahead (do nothing)

        return len(stack)