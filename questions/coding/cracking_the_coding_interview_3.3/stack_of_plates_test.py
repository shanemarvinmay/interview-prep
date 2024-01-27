from stack_of_plates_solution import SetOfStacks

def test_push_under_limit():
    stacks = SetOfStacks()

    for i in range(stacks.stack_limit):
        stacks.push(i)

    assert len(stacks.stacks) == 1 and stacks.stacks[-1][-1] == stacks.stack_limit - 1 

def test_push_over_limit(): 
    stacks = SetOfStacks()

    for i in range(stacks.stack_limit + 1):
        stacks.push(i)

    assert len(stacks.stacks) == 2 and stacks.stacks[-1][-1] == stacks.stack_limit 

def test_pop_empty():
    stacks = SetOfStacks()

    assert stacks.pop() is None

def test_pop_full_and_empty_stacks():
    stacks = SetOfStacks()

    for i in range(stacks.stack_limit + 1):
        stacks.push(i)

    assert stacks.pop() == stacks.stack_limit and len(stacks.stacks) == 2
    assert stacks.pop() == stacks.stack_limit - 1 and len(stacks.stacks) == 1 

def test_pop_at():
    stacks = SetOfStacks()

    stacks.push(0)

    assert stacks.pop_at(1) is None
    assert stacks.pop_at(0) == 0