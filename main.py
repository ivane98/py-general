from pythonds.basic import Stack

def devideby2(decnum):
    remstack = Stack()

    while decnum > 0:
        rem = decnum % 2
        remstack.push(rem)
        decnum = decnum // 2
    

    binString = ''

    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())


    return binString


print(devideby2(1))