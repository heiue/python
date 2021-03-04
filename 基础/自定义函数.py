import example

def ceshi1(param1):
    param1['a'] = 1
    return param1


def ceshi2(param1):
    print(param1)


def ceshi3(*params):
    print(params)


def ceshi4(param1, param2, **params):
    dict = {}
    dict['param1'] = param1
    dict['params2'] = param2
    for key, value in params.items():
        dict[key] = value
    print(dict)

def updateInt(a):
    a = 5

def updateList(aList):
    aList.append(2)

g = lambda x:x+2

if __name__ == '__main__':
    param_list = {}
    ceshi1(param_list)
    ceshi2(param_list)

    ceshi3('a', 'b', 'c')

    ceshi4('haha', 'xixi', age='18', sex=1, like='来来来')

    example.ceshi()
    print(g(5))

    a = 1
    updateInt(a)
    print(a)

    listEx = [1,2,3]
    updateList(listEx)
    print(listEx)