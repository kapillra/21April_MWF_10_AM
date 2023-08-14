def password_generate(sm=None, caps=None, nums=None, sp_chars=None, length=8):
    import random
    
    small = ''
    capital = ''
    each_len = 2
    if length:
        if length % 2:
            length = length + 1
            each_len = length / 4
        else:
            each_len = length / 4
    each_len = random._ceil(each_len)

    for c in range(97, 123):
        small += chr(c)
    else:
        capital = small.upper()

    numbers = ''
    for n in range(48, 58):
        numbers += chr(n)
    
    special_chars = ''
    avoid_sp_chars = [',',"'",'"',"(",")","[","]","{","}",".",":",";","<",">","/","\\"]
    for i in range(33, 96):
        if not chr(i).isalnum() and not chr(i) in avoid_sp_chars:
            special_chars += chr(i)
    
    # print(special_chars)

    # print(random.choices(small + capital + numbers + special_chars, k=8))

    # print(random.choices(small, k=2))
    # print(random.choices(capital, k=2))
    # print(random.choices(numbers, k=2))
    # print(random.choices(special_chars, k=2))

    if length:
        l = [*small + capital + numbers + special_chars]
        random.shuffle(l)
        pwd = random.choices(l, k=length)
    else:
        pwd = random.choices(small, k=sm) + random.choices(capital, k=caps) + random.choices(numbers, k=nums) + random.choices(special_chars, k=sp_chars)
    
    # print(''.join(pwd))
    # random.shuffle(pwd)
    # print(''.join(pwd))


# password_generate(length=10)