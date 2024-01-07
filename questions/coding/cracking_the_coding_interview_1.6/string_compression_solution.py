def string_compression(s):
    if len(s) < 1:
        return s
    compressed_str_builder = []
    char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] != char:
            compressed_str_builder.append(f'{char}{count}')
            char = s[i]
            count = 1
        else:
            count += 1
    compressed_str_builder.append(f'{char}{count}')
    
    compressed_str = ''.join(compressed_str_builder)

    return compressed_str if len(compressed_str) < len(s) else s