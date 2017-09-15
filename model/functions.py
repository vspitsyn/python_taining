def clear_double_space(s):
    index_space = s.find('  ')
    if index_space > -1:
        s = clear_double_space(s[0:index_space] + s[index_space + 1:len(s)])
    return s