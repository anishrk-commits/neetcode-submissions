class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        sorted_position = sorted(position)
        # print(sorted_position)
        # sorted_position.index(position)

        fleet = 0

        current_fleet_time = None
        
        while True:
            if len(sorted_position) == 0:
                break
            currentpos = sorted_position.pop()
            time = (target - currentpos) / speed[position.index(currentpos)]
            
            if len(sorted_position) + 1 == len(position):
                current_fleet_time = time
                fleet += 1
                continue

            if(current_fleet_time >= time):
                continue
            else:
                fleet += 1
                current_fleet_time = time
        
        return fleet


        

        


