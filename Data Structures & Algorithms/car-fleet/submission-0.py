class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []

        # formula, time = (target-position)//speed
        for i in range(len(position)):
            time = (target-position[i])//speed[i]
            if time not in fleet:
                fleet.append(time)
        return len(fleet)