'''Testing the hash table implementation in python.'''
from hash_table_list import HashTableList
import pytest

# Hash Table list test
def test_hash_table_list_set_get_element():
    hash_table = HashTableList()
    
    hash_table.set('one', 1)

    assert hash_table.get('one') == 1, 'hash_table key "one" has the value of 1'

def test_hash_table_list_get_key_not_found():
    hash_table = HashTableList()

    with pytest.raises(KeyError) as key_not_found_exception:
        hash_table.get('some key')

    assert 'The key:some key is not found in the hashmap'in str(key_not_found_exception.value)
