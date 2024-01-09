# Numbers can be formatted with '_'
formatted_number = 1_234_567
digusting_number = 1234567

# List comprehension
powers_of_two = [2 ** exponent for exponent in range(30)]

# Copy list 
some_list = ['some', 'list', 'items']
# Deep copies
a_copy = some_list[:]
another_copy = some_list.copy()
another_deep_copy = list(some_list)
# Shallow copy
shallow_copy = some_list

# Tuple with only one element
only_on = ('element',)

# Removing/Deleting from a dictionary
a_dict = {'key': 'value', 'another_key': 'another_value'}
del a_dict['another_key']

# Get nonexistant key from dict without error
a_dict.get('another_key', 'The key:"another_key" isn\'t in a_dict. You should try... another key *que laugh track*')

# Looping through dicts
for key, value in a_dict.items():
    # print(key, value)
    pass
for key in a_dict.keys():
    # print(key)
    pass
for value in a_dict.values():
    # print(value)
    pass

# Taking an unknown numbers of arguments *ars
def print_car_features(car_name, *features):
    '''Print a car and it's features.'''
    print(car_name, end=': ')
    print(', '.join(features))
# print_car_features('Batmobile', 'Jet engine', 'Bulletproof windows', 'Cup holders', 'Car seat for Robin')

if __name__ == '__main__':
    print(some_list == a_copy == another_copy)
    print(some_list is another_deep_copy, some_list is shallow_copy)
    print(f'some_list:{some_list}')
    print(f'a_copy:{a_copy}')
    print(f'another_copy:{another_copy}')
    print(f'another_deep_copy:{another_deep_copy}')
    print(f'shallow_copy:{shallow_copy}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    some_list[2] = 'item'
    some_list.append('changed')
    print(f'some_list:{some_list}')
    print(f'a_copy:{a_copy}')
    print(f'another_copy:{another_copy}')
    print(f'another_deep_copy:{another_deep_copy}')
    print(f'shallow_copy:{shallow_copy}')