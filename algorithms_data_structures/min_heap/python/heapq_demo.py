from random import randint

import heapq

nums = []

for _ in range(5):
    nums.append(randint(0, 100))

print(f'nums:{nums}')

heapq.heapify(nums)
print(f'nums after turning into heap (heapify):{nums}')

print('Adding -1 to the heap')
heapq.heappush(nums, -1)
print(f'nums:{nums}')
print('Adding 101 to the heap')
heapq.heappush(nums, 101)
print(f'nums:{nums}')

print(f'Popping the smallest num from the heap:{heapq.heappop(nums)}')
print(f'nums:{nums}')

print(f'Getting the 3 largest nums from the heap:{heapq.nlargest(3, nums)}')
print(f'nums:{nums}')

print(f'Getting the 4 smallest nums from the heap:{heapq.nsmallest(4, nums)}')
print(f'nums:{nums}')