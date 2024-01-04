class HashTableList:
    '''This is an implementation of Hash Table using lists in python.'''
    def __init__(self):
        self.list = [[]] * 100

    def set(self, key, value):
        key = hash(key)
        idx = key % len(self.list)
        self.list[idx].append([key, value])  

    def get(self, key):
        key_hash = hash(key)
        idx = key_hash % len(self.list)
        for key_value in self.list[idx]:
            if key_hash == key_value[0]:
                return key_value[1]
        raise KeyError(f'The key:{key} is not found in the hashmap')