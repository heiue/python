str = '13521282025'

phone = str.replace(str[3:7], '*' * 4)

print(phone)

print(str.find('20'))

str = 'i {} want {} you'
print(str.format('1', '2'))

# 排序 sorted()
print('排序')
num_list = [6, 3, 5, 1, 2, 4, 6, 9]
print(sorted(num_list))
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
num_list = [6, 3, 5, 1, 2, 4, 6, 9]
num_list.reverse()
print(num_list)
print('排序end')

str = 'abcdefghijklmn'

for a,b in zip(num_list, str):
    print(b, a)

# 列表解析式
b = [i for i in range(1, 11)]
print(b)

# 循环列表的key 和 value
list = ['a', 'b', 'c', 'd', 'e']
for num,str in enumerate(list):
    print(str, 'is', num + 1)


strEx = "hello"
print(strEx.capitalize())

print(strEx.center(10, '-'))

print(strEx.count('l', 2))

print(strEx.encode())
strExBy = strEx.encode()
print(strExBy.decode())

print(strEx.endswith('llo', 2))

print(strEx.find('a'))
print(strEx.index('e'))

strEx = '为什么qqw'
print(strEx.isalnum())
print(strEx.isalpha())

strEx = '123'
print(strEx.isdigit())

strEx = 'hello123'
print(strEx.islower())

strEx = 'abc'
print(strEx.isspace())

print(strEx.title())
print(strEx.capitalize().istitle())

strEx = ','
print(strEx.join('abc'))

print(len(strEx))

strEx = 'abc'
print(strEx.ljust(10, '-'))

strEx = 'abcDefG '
print(strEx.lower())

print(strEx.lstrip('ab'))

strEx = 'abc'
maket = str.maketrans('abc', '123')
print(maket)
print(strEx.translate(maket))

strEx = '13521282025'
print(strEx.replace('2', '*', 3))

strEx = 'a,b,c,d,e'
print(strEx.split(',', 3))

strEx = 'hello\nmy'
print(strEx.splitlines())

strEx = 'hello'
print(strEx.startswith('he'))

strEx = 'Hello'
print(strEx.swapcase())

print(strEx.upper())

print(strEx.zfill(10))

strEx = '10'
print(strEx.isdecimal())