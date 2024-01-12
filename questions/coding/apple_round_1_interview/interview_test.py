import pytest

from interview import metrics, precision, recall

@pytest.fixture
def normal_responses():
    responses = [{'got': True, 'expected': True}, {'got': True, 'expected': False}, {'got': False, 'expected': True}]
    return responses

def test_metrics_exceptions():
    pass

def test_metrics_calc_correctly():
    pass

def test_precision_calc_correctly(normal_responses):
    assert precision(normal_responses) == 0.5

def test_precision_zero_returned():
    assert precision([]) == 0