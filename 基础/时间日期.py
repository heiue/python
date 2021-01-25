from datetime import datetime
import time

print(datetime.utcnow())

print(datetime.today().timestamp())

print(int(time.time()))

print(time.localtime())

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取下面代码执行时间
start = time.perf_counter() * 1000
a = []
for i in range(1, 11):
    a.append(i)
print('执行时间是 ', time.perf_counter() * 1000 - start)