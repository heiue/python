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


if __name__ == '__main__':
    param_list = {}
    ceshi1(param_list)
    ceshi2(param_list)

    ceshi3('a', 'b', 'c')

    ceshi4('haha', 'xixi', age='18', sex=1, like='来来来')
