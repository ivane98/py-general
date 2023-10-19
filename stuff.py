from pythonds.basic import Stack

def devideby2(decnum):
    remstack = Stack()

    while decnum > 0:
        rem = decnum % 2
        remstack.push(rem)
        print(rem)
        decnum = decnum // 2
    

    binString = ''

    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())


    return binString

def base_converter(decnum, base):
    digits = '0123456789ABCDEF'

    remstack = Stack()

    while decnum > 0:
        rem = decnum % base
        remstack.push(rem)
        decnum = decnum // base

    new_string = ''

    while not remstack.isEmpty():
        new_string = new_string + digits[remstack.pop()]

    return new_string        

# print(base_converter(256, 16))


