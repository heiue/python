# 列表
print('列表')
listEx = []
print(listEx)
listEx = [n for n in range(5, 20)]
print(listEx)
print(listEx[1:6:3])

listEx = [1 for n in range(5)]
listEx = [1] * 5
listEx.insert(1, 'jem')
listEx.append('bob')
listEx.append(['lis', 'hoe'])
print(listEx)
listEX = [1, 'a', 2, 2, 3, 5]
# 增
listEX.insert(1, 100)
print(listEX)
listEX.extend('lsie')
listEX.extend(['a', 5])
print(listEX)

listEX.remove(2)
print(listEX)

def sortSecond(item):
    return item[1]
num_list = [[1,2], [3,4], [2,3], [5,9]]
num_list.sort(key=sortSecond)
print(num_list)

del listEX[0:2]
print(listEX)
print(len(listEX))

foods = ['pizza', 'falafel']
print(foods)
my_foods = foods
print(my_foods)
foods.append('ice cream')
print(my_foods)
print('列表end')
# 字典
print('字典')
dictEx = {'a':1, 'b':2}
print(dictEx)
dictEx[1] = 'abc'
print(dictEx)
new_dictEx = dictEx.keys()
print(list(new_dictEx))
print(dictEx.values())

listEx = [('python', 1), ('php', 2), ('golang', 3)]
print(dict(listEx))

dictEx = {x: x**2 for x in (2, 4, 6)}
print(dictEx)
print(2**3)
dictEx = dict(python=1, php=2, golang=3)
print(dictEx)
dictEx = {'python': 'one', 'php': 'two', 'python': 'three'}
print(dictEx)
dictEx = {(1, 2): 1, 's': 'bbb'}
print(dictEx)
print(list(dictEx.keys()))
exit()
# 增
dictEx['c'] = 3
print(dictEx)
dictEx.update({'t':1, 'd': "66"})
print(dictEx)

del dictEx['b']
print(dictEx)

dictEx = {'jen': 'python', 'sarch': 'c', 'phil': 'python'}
for name in dictEx.keys():
    print(name.title())

print(set(dictEx.keys()))
print(set(dictEx.values()))
print('字典end')
# 元组
print('元组')
letter = ('a', 'b', 'c', 'd')
print(letter)
print(letter[1])
listEX = [1, 2, 3]
letter = ([1, 2, 3], 'a')
letter[0][2] = 5
print({1, 2, 3, 1, 3})

# 字符串
stringEx = "'aaaaa'"
print(stringEx)
stringEx = '''
my code
oh, this is 'cat'
yes, l like "it"
'''

stringEx = """
aaa
bbb
ccc
"""
print(stringEx)
##注释
"""
的撒发的
"""

stringExS = 'abcdefg'
print(stringExS[1:3])

stringExS = 'abcdefgh'
for s in stringExS:
    print(s)


# 集合
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a - b)
print(b - a)
print(a | b)
print(a & b)
print(a ^ b)
