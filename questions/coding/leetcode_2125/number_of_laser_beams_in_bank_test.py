from number_of_laser_beams_in_bank_solution import Solution

import pytest

@pytest.fixture()
def number_of_beams():
    s = Solution()
    return s.numberOfBeams

# Test multiple rows of beams
def test_number_of_beams_multiple_rows(number_of_beams):
    bank = [
        "011001",
        "000000",
        "010100",
        "001000"]
    
    assert number_of_beams(bank) == 8

# Test one row of securiy devices with no following ends to make a beam.
def test_number_of_beams_one_row_devices(number_of_beams):
    bank = [
        "000",
        "111",
        "000"]
    
    assert number_of_beams(bank) == 0
