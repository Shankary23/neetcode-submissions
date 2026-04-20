class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        order = sorted(zip(position,speed), reverse = True)
        # print(position)
        # formula, time = (target-position)//speed
        for i,j in order:
            time = (target-i)/j
            if not fleet or time > fleet[-1]:
                fleet.append(time)
                print(fleet)
        return len(fleet)
