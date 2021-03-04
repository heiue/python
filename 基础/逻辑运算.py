album = ['cc', 'aa', 'bb']

if 'aa' in album:
    print(1)
else:
    print(2)

b = 1
c = (a := 12) + b
print(a, c)

a = 60
b = 13

print(a&b)
print(~a)
print(a<<5)
print(bin(1920))
print(a>>1)

if a > 1 or b < 5:
    print(1)


intEx = 1
intEx2 = 0
while intEx == 1:
    if intEx2 > 5:
        break
    intEx2 += 1
print(intEx2)

intEx = 6
while intEx > 5:
    intEx -= 1
    print('intEx 大于 5')
else:
    print('intEx 不大于 5')

listEx = ['python', 'php', 'golang']
stringEx = 'python'
dictEx = {'a': 1, 'b': 2, 'c': 3}
for item in dictEx:
    print(item)
else:
    print('循环结束')