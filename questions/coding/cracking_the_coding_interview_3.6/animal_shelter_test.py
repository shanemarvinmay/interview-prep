from animal_shelter_solution import *
from time import time

import pytest

@pytest.mark.parametrize('num_dogs, message', [
    (0, 'No dogs.'),
    (1, 'Only one dog.'),
    (5, 'Multiple dogs.')
])
def test_dequeue_dog(num_dogs, message):
    animal_shelter = AnimalShelter()

    expected = []
    for i in range(num_dogs):
        # Adding i to offset the timestamps.
        timestamp = round(time(), 2) + i
        expected.append(timestamp)
        animal_shelter.enqueue(AnimalType.DOG, timestamp)
    
    for timestamp in expected:
        dog = animal_shelter.dequeue_dog()
        assert dog.timestamp == timestamp, message

    # Asserting there is no more dogs.
    assert animal_shelter.oldest_dog is None and animal_shelter.newest_dog is None, message

@pytest.mark.parametrize('num_cats, message', [
    (0, 'No cats.'),
    (1, 'Only one cat.'),
    (5, 'Multiple cats.')
])
def test_dequeue_cat(num_cats, message):
    animal_shelter = AnimalShelter()

    expected = []
    for i in range(num_cats):
        # Adding i to offset the timestamps.
        timestamp = round(time(), 2) + i
        expected.append(timestamp)
        animal_shelter.enqueue(AnimalType.CAT, timestamp=timestamp)
        
    for timestamp in expected:
        cat = animal_shelter.dequeue_cat()
        assert cat.timestamp == timestamp, message

    # Asserting there is no more cats.
    assert animal_shelter.oldest_cat is None and animal_shelter.newest_cat is None, message

@pytest.mark.parametrize('num_dogs, num_cats, message', [
    (0, 0, 'No animals.'),
    (1, 0, 'Only dogs'),
    (0, 1, 'Only cats'),
    (2, 2, 'Both cats and dogs.')
])
def test_dequeue_any(num_dogs, num_cats, message):
    animal_shelter = AnimalShelter()

    expected = []
    for i in range(num_dogs + num_cats):
        # Adding i to offset the timestamps.
        timestamp = round(time(), 2) + i
        expected.append(timestamp)
        # This will ensure that half the dogs are 'older' than the cats, and vice versa.
        animal_type = AnimalType.DOG if i % 2 else AnimalType.CAT
        animal_shelter.enqueue(animal_type, timestamp)

    for timestamp in expected:
        animal = animal_shelter.dequeue_any()
        assert animal.timestamp == timestamp, message

    # Asserting there is no more dogs.
    assert animal_shelter.oldest_dog is None and animal_shelter.newest_dog is None, message
    # Asserting there is no more cats.
    assert animal_shelter.oldest_cat is None and animal_shelter.newest_cat is None, message