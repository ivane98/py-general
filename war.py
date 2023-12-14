def rot13(message):
    l1 = 'abcdefghijklmnopqrstuvwxyz'
    l2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    res = ''

    for i in message:
        if i in l2:
            if l2.index(i)+12 > len(l2):
               nl = len(l2) - l2.index(i)
               res +=  l2[nl]
            res += l2[l2.index(i)+12]
        elif l1.index(i)+12 > len(l1):
               nl = len(l1) - l1.index(i) - 1
               res +=  l1[nl]
        else:
            res += l1[l1.index(i)+13]

    return res

print(rot13('s'))

