# 列表
print('列表')
list = [1, 'a', 2, 2, 3, 5]
# 增
list.insert(1, 100)
print(list)
list.extend(['a', 5])
print(list)

list.remove(2)
print(list)

del list[0:2]
print(list)
print(len(list))

foods = ['pizza', 'falafel']
print(foods)
my_foods = foods
print(my_foods)
foods.append('ice cream')
print(my_foods)
print('列表end')
# 字典
print('字典')
dict = {'a':1, 'b':2}
print(dict)
# 增
dict['c'] = 3
print(dict)
dict.update({'t':1, 'd': "66"})
print(dict)

del dict['b']
print(dict)

dict = {'jen': 'python', 'sarch': 'c', 'phil': 'python'}
for name in dict.keys():
    print(name.title())

print(set(dict.keys()))
print(set(dict.values()))
print('字典end')
# 元组
print('元组')
letter = ('a', 'b', 'c', 'd')
print(letter)
print(letter[1])
print({1, 2, 3, 1, 3})