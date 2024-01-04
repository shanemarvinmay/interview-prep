def urlify(s):
    string_builder = []
    url_space_char_needed = False

    s = s.strip()
    for ltr in s:
        if ltr != ' ':
            if url_space_char_needed:
                string_builder.append('%20')
                url_space_char_needed = False
            string_builder.append(ltr)
        else:
            url_space_char_needed = True
    
    return ''.join(string_builder)