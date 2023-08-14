def add(x, y, *n):
    '''returns an addition of x and y + *n'''
    s = x + y
    for i in n:
        s += i
    return s