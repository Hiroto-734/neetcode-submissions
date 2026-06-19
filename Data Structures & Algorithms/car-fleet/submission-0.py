class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse= True)
        time_list = []

        for pos, speed in cars:
            time_list.append( (target - pos) / speed )
        
        index = 0
        count = 1
        for idx, time in enumerate(time_list):
            if time_list[index] < time:
                count += 1
                index = idx
        
        return count 
