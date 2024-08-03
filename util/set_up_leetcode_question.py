from leetcode_title_to_file_name import leetcode_title_to_file_name

import os
cwd = os.getcwd()
print(f'cwd:{cwd}')

raw_input = input("Enter leetcode number and title e.g.:'427. Construct Quad Tree'\n")

num, title = raw_input.split('.', 1)
title = title.strip()
title = leetcode_title_to_file_name(title)

# Making problem dir.
path = os.path.join(cwd, 'questions', 'coding', f'leetcode_{num}')
os.mkdir(path)

# Make __init__.
with open(f'{path}/__init__.py', 'w') as f:
    f.write('')

# Writing source and test file.
with open(f'{path}/{title}.py', 'w') as f:
    f.write('')
with open(f'{path}/test_{title}.py', 'w') as f:
    f.write('')

print('Done.')