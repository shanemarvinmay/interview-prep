from enum import Enum
from time import time

class AnimalType(Enum):
        DOG = 1
        CAT = 2

class AnimalShelter:
    class Node:
        def __init__(self, timestamp):
            self.timestamp = timestamp
            self.next = None

    def __init__(self):
        self.oldest_dog = self.newest_dog = None
        self.oldest_cat = self.newest_cat = None
    
    def enqueue(self, type, timestamp=None):
        timestamp = round(time(), 2) if timestamp is None else timestamp
        new_node = self.Node(timestamp)
        if type is AnimalType.DOG:
            # Queue is empty.
            if self.oldest_dog is None:
                self.oldest_dog = self.newest_dog = new_node
            # Queue is not empty.
            else:
                self.newest_dog.next = new_node
                self.newest_dog = new_node
        else:
            # Queue is empty.
            if self.oldest_cat is None:
                self.oldest_cat = self.newest_cat = new_node
            # Queue is not empty.
            else:
                self.newest_cat.next = new_node
                self.newest_cat = new_node

    def dequeue_any(self):
        # One or both queues are empty.
        if self.oldest_cat is None and self.oldest_dog is None:
            return
        elif self.oldest_cat is None and self.oldest_dog:
            return self.dequeue_dog()
        elif self.oldest_cat and self.oldest_dog is None:
            return self.dequeue_cat()
        # return whichever is oldest
        if self.oldest_dog.timestamp < self.oldest_cat.timestamp:
            return self.dequeue_dog()
        return self.dequeue_cat()

    def dequeue_dog(self):
        dog = self.oldest_dog
        # Only one dog in queue.
        if self.oldest_dog == self.newest_dog:
            self.oldest_dog = self.newest_dog = None
        # Multiple dogs in queue.
        else:
            self.oldest_dog = self.oldest_dog.next
        return dog

    def dequeue_cat(self):
        cat = self.oldest_cat
        # Only one cat in queue.
        if self.oldest_cat == self.newest_cat:
            self.oldest_cat = self.newest_cat = None
        # Multiple cats in queue.
        else:
            self.oldest_cat = self.oldest_cat.next
        return cat
