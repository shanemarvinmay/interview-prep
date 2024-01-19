class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        cities = set()
        
        for path in paths:
            cities.add(path[0])

        for path in paths:
            destination_city = path[1]
            if destination_city not in cities:
                return destination_city
