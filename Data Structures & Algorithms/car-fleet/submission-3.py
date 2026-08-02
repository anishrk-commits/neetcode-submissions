class Solution():
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed))  # O(n log n), preserves pairing
        fleet = 0
        current_fleet_time = 0

        for pos, spd in reversed(pairs):      # O(n)
            time = (target - pos) / spd       # O(1) lookup
            if time > current_fleet_time:
                fleet += 1
                current_fleet_time = time

        return fleet