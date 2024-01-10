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

# Taking an unknown numbers of arguments as a list (*ars)
def print_car_features(car_name, *features):
    '''Print a car and it's features.'''
    print(car_name, end=': ')
    print(', '.join(features))
# print_car_features('Batmobile', 'Jet engine', 'Bulletproof windows', 'Cup holders', 'Car seat for Robin')

# Taking an unknown numbers of arguments as a dict (**kwargs)
def create_new_job(title, **job_details):
    job_details['job_title'] = title
    for details, value in job_details.items():
        print(details, value)
    return job_details
# create_new_job('ml engineer', money='a lot', location='hybrid')

# After a successful try, you can use an else
def try_except_else_example(throw_exception=False):
    try:
        print(0 / 0 if throw_exception else 1)
    except ZeroDivisionError:
        print('Caught you trying to divide by zero. Tsk..tsk... Rookie mistake')
    else:
        print('Nice job not dividing by zero.')

# Test with unittest.
import unittest
import math
def func_to_test(num):
    try:
        return round(num ** num  / math.log(num), 2)
    except ValueError:
        raise ValueError("Math domain error")
class ExampleTestCase(unittest.TestCase):
    """Example test case for func_to_test."""
    def setUp(self) -> None:
        # Do some stuff the will happen before the tests start.
        return super().setUp()
    def test_func_to_test_returns_correct_number(self):
        """Test that func_to_test(2) returns 5.77"""
        self.assertEqual(func_to_test(2), 5.77)
    def test_func_to_test_throws_exception(self):
        with self.assertRaises(ValueError):
         func_to_test(0)

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
    print(func_to_test(2))
    unittest.main()
