class UndergroundSystem:

    def __init__(self):
        self.customer_map = dict()
        self.trip_map = dict()

    def checkIn(self, id: int, stationName: str, time: int) -> None:
        self.customer_map[id] = {'station': stationName, 'start': time}

    def checkOut(self, id: int, stationName: str, time: int) -> None:
        from_station = self.customer_map[id]['station']
        duration = time - self.customer_map[id]['start']
        if from_station not in self.trip_map:
            self.trip_map[from_station] = dict()
        if stationName not in self.trip_map[from_station]:
            self.trip_map[from_station][stationName] = []
        self.trip_map[from_station][stationName].append(duration)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = sum(self.trip_map[startStation][endStation])
        qty = len(self.trip_map[startStation][endStation])
        return total / qty


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)