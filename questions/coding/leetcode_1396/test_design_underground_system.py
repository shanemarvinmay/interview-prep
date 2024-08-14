from questions.coding.leetcode_1396.design_underground_system import UndergroundSystem

import pytest

@pytest.fixture()
def sol():
    return UndergroundSystem()


def test_all(sol):
    func_calls = ["checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
    args = [[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
    expected = [None,None,None,None,None,None,14.00000,11.00000,None,11.00000,None,12.00000]
    for i in range(len(func_calls)):
        if func_calls[i] == "checkIn":
            id, station, time = args[i]
            got = sol.checkIn(id, station, time)
        elif func_calls[i] == "checkOut":
            id, station, time = args[i]
            got = sol.checkOut(id, station, time)
        else:
            start, end = args[i]
            got = sol.getAverageTime(start, end)
        assert got == expected[i]
