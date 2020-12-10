import math

print(math.cos(5))

try:
    raise Exception('错误')
except Exception as e:
    print(e)