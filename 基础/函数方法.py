str = '13521282025'

phone = str.replace(str[4:7], '*' * 4)

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
