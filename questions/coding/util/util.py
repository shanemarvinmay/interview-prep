def leetcode_title_to_file_name(title):
    title = title.lower()
    title = title.replace(' ', '_')
    return title

title = input('Enter leetcode title:')
print('file_name:', leetcode_title_to_file_name(title))