class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new = zip(position,speed)
        newpos = sorted(new, key=lambda x:-x[0])
        fleet_count = 0
        last_fleet = None
        for i in range(len(newpos)):
            time = (target - newpos[i][0]) / newpos[i][1]
            if last_fleet == None:
                fleet_count +=1
                last_fleet = time
            elif last_fleet < time:
                last_fleet = time
                fleet_count +=1
        return fleet_count
        