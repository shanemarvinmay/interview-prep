from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        output = []
        # Sort by height
        people.sort(key=lambda person: (-person[0], person[1]))
        for person in people:
            output.insert(person[1], person)
        return output
