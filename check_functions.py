st = '      te          st         '
def clear_doble_space(s):
    index_space = s.find('  ')
    if index_space>-1:
        s = clear_doble_space(s[0:index_space] + s[index_space+1:len(s)])
    # else:
    #     return s
    return s
print('d'+clear_doble_space(st)+'d')
