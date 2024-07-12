from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0

        jug = capacity

        for i in range(len(plants)):
            if plants[i] > jug:
                # Walk back to the river.
                steps += i
                # Fill up watering jug
                jug = capacity
                # Walk back to the plant.
                steps += i
            # Water the plant.
            jug -= plants[i]
        
        steps += len(plants)

        return steps