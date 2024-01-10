f = open('names.txt')

# print(f.read(4))

# print(f.readlines())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open('c.txt')
    print(f.read())

except:
    print('no such file')

finally:
    f.close()